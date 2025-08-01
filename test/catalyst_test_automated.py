#!/usr/bin/env python3
"""
Catalyst Automated Test Suite
Fully automated - starts server, runs tests, generates report, shuts down
No human interaction required
"""
import json
import os
import sys
import time
import subprocess
import requests
import signal
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Add repo to path
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

# Load environment variables from .env file
load_dotenv(REPO_ROOT / ".env")

# Test queries
TEST_QUERIES = [
    "list catalyst devices",
    "get catalyst projects",
    "catalyst get physical topology",
    "catalyst get application policy",
    "catalyst get sites",
    "catalyst site health",
    "catalyst packages",
    "catalyst release info",
    "catalyst config summary"
]

class AutomatedCatalystTester:
    def __init__(self, port: int = 8004):  # Use 8004 as requested
        self.port = port
        self.base_url = f"http://localhost:{port}"
        self.server_process = None
        self.results = []
        self.pid_file = REPO_ROOT / ".run" / f"test_agent_{port}.pid"
        self.log_file = REPO_ROOT / ".run" / f"test_agent_{port}.log"
        
    def start_server(self) -> bool:
        """Start the FastAPI server programmatically"""
        print(f"🚀 Starting FastAPI server on port {self.port}...")
        
        # Ensure .run directory exists
        self.pid_file.parent.mkdir(exist_ok=True)
        
        # Build the command
        env = os.environ.copy()
        env["PYTHONPATH"] = str(SRC_DIR)
        # Disable OpenTelemetry for testing
        env["OTEL_SDK_DISABLED"] = "true"
        
        # Start uvicorn directly (bypassing the interactive menu)
        # Use the virtual environment's python if available
        venv_python = Path.home() / "env" / "bin" / "python"
        python_exe = str(venv_python) if venv_python.exists() else sys.executable
        
        cmd = [
            python_exe, "-m", "uvicorn",
            "app.main:app",
            "--host", "0.0.0.0",
            "--port", str(self.port),
            "--log-level", "error"  # Reduce noise
        ]
        
        # Open log file for server output
        with open(self.log_file, "w") as log:
            self.server_process = subprocess.Popen(
                cmd,
                cwd=str(SRC_DIR),
                env=env,
                stdout=log,
                stderr=log,
                preexec_fn=os.setsid  # Create new process group
            )
        
        # Write PID for cleanup
        self.pid_file.write_text(str(self.server_process.pid))
        
        # Wait for server to be ready
        max_retries = 30
        for i in range(max_retries):
            try:
                response = requests.get(f"{self.base_url}/docs", timeout=2)
                if response.status_code == 200:
                    print(f"✅ Server ready on port {self.port}")
                    return True
            except:
                pass
            time.sleep(1)
            
        print("❌ Server failed to start")
        self.stop_server()
        return False
    
    def stop_server(self):
        """Stop the FastAPI server"""
        if self.server_process:
            print("🛑 Stopping server...")
            try:
                # Kill the entire process group
                os.killpg(os.getpgid(self.server_process.pid), signal.SIGTERM)
                self.server_process.wait(timeout=5)
            except:
                # Force kill if needed
                try:
                    os.killpg(os.getpgid(self.server_process.pid), signal.SIGKILL)
                except:
                    pass
            
            # Cleanup
            self.pid_file.unlink(missing_ok=True)
            print("✅ Server stopped")
    
    def test_query(self, query: str) -> Dict:
        """Test a single query"""
        print(f"\n📝 Testing: {query}")
        start_time = time.time()
        
        # Use longer timeout for queries that might return large datasets
        timeout = 60  # Default timeout set to 60 seconds for all queries
        
        try:
            response = requests.post(
                f"{self.base_url}/chat",
                json={"message": query},
                timeout=timeout
            )
            
            elapsed_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                response_text = data.get("response", "")
                
                # Detect function from response
                function_called = self._detect_function(query, response_text)
                
                print(f"   ✅ Success - Function: {function_called} ({elapsed_time:.2f}s)")
                
                return {
                    "query": query,
                    "status": "success",
                    "function_called": function_called,
                    "response_preview": response_text[:200] + "..." if len(response_text) > 200 else response_text,
                    "elapsed_time": elapsed_time
                }
            else:
                error_msg = f"HTTP {response.status_code}"
                print(f"   ❌ Failed - {error_msg}")
                
                return {
                    "query": query,
                    "status": "failed",
                    "error": error_msg,
                    "elapsed_time": elapsed_time
                }
                
        except Exception as e:
            elapsed_time = time.time() - start_time
            error_msg = str(e)
            print(f"   ❌ Failed - {error_msg}")
            
            return {
                "query": query,
                "status": "failed",
                "error": error_msg,
                "elapsed_time": elapsed_time
            }
    
    def _detect_function(self, query: str, response: str) -> str:
        """Detect which function was likely called"""
        query_lower = query.lower()
        
        if "device" in query_lower:
            return "getDeviceList"
        elif "project" in query_lower:
            return "getProject_s_Details"
        elif "topology" in query_lower:
            return "getPhysicalTopology"
        elif "application policy" in query_lower:
            return "getApplicationPolicy"
        elif "site" in query_lower:
            if "health" in query_lower:
                return "getSiteHealth"
            else:
                return "getSites"
        elif "package" in query_lower:
            return "ciscoDNACenterPackagesSummary"
        elif "release" in query_lower:
            return "ciscoDNACenterReleaseSummary"
        elif "config" in query_lower and "summary" in query_lower:
            return "ciscoDNACenterNodesConfigurationSummary"
        
        return "Unknown"
    
    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "="*60)
        print("Running Catalyst Test Suite")
        print("="*60)
        
        for query in TEST_QUERIES:
            result = self.test_query(query)
            self.results.append(result)
    
    def generate_report(self) -> bool:
        """Generate test report and return success status"""
        successful = [r for r in self.results if r["status"] == "success"]
        failed = [r for r in self.results if r["status"] == "failed"]
        
        print("\n" + "="*60)
        print("TEST RESULTS SUMMARY")
        print("="*60)
        print(f"Total Tests: {len(self.results)}")
        print(f"Successful: {len(successful)} ✅")
        print(f"Failed: {len(failed)} ❌")
        print(f"Success Rate: {len(successful)/len(self.results)*100:.1f}%")
        
        # Save detailed report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = REPO_ROOT / "test" / f"catalyst_automated_results_{timestamp}.json"
        
        report_data = {
            "test_date": datetime.now().isoformat(),
            "server_port": self.port,
            "summary": {
                "total": len(self.results),
                "successful": len(successful),
                "failed": len(failed),
                "success_rate": f"{len(successful)/len(self.results)*100:.1f}%"
            },
            "environment": {
                "DNACENTER_BASE_URL": "Set" if os.getenv("DNACENTER_BASE_URL") else "Not set",
                "DNACENTER_USERNAME": "Set" if os.getenv("DNACENTER_USERNAME") else "Not set",
                "DNACENTER_PASSWORD": "Set" if os.getenv("DNACENTER_PASSWORD") else "Not set"
            },
            "results": self.results
        }
        
        with open(report_file, "w") as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: {report_file}")
        
        # Print failed queries for easy debugging
        if failed:
            print("\n" + "-"*60)
            print("FAILED QUERIES:")
            print("-"*60)
            for result in failed:
                print(f"❌ {result['query']}: {result.get('error', 'Unknown error')}")
        
        return len(failed) == 0
    
    def run(self) -> bool:
        """Main execution flow"""
        print(f"🤖 Catalyst Automated Test Suite")
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🔧 Using port: {self.port}")
        
        try:
            # Start server
            if not self.start_server():
                return False
            
            # Give server a moment to fully initialize
            time.sleep(2)
            
            # Run tests
            self.run_all_tests()
            
            # Generate report
            success = self.generate_report()
            
            return success
            
        finally:
            # Always stop server
            self.stop_server()


def main():
    """Main entry point"""
    # Parse command line args
    port = 8004  # Default port as requested
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except:
            print(f"Usage: {sys.argv[0]} [port]")
            sys.exit(1)
    
    # Check environment
    required_vars = ["DNACENTER_BASE_URL", "DNACENTER_USERNAME", "DNACENTER_PASSWORD"]
    missing = [v for v in required_vars if not os.getenv(v)]
    if missing:
        print("⚠️  WARNING: Missing environment variables:")
        for var in missing:
            print(f"   - {var}")
        print("\nTests may fail without proper credentials.")
        print("Add these to your .env file or export them.\n")
    
    # Run automated test
    tester = AutomatedCatalystTester(port=port)
    success = tester.run()
    
    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n⚠️  Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    # Activate virtual env if needed
    activate_script = Path.home() / "env" / "bin" / "activate_this.py"
    if activate_script.exists():
        exec(open(activate_script).read(), {'__file__': str(activate_script)})
    
    main()
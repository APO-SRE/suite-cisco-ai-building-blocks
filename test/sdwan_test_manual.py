#!/usr/bin/env python3
"""
SD-WAN Chat Interface Test Suite - Standalone Version
Tests SD-WAN queries directly via HTTP API calls
"""
import json
import os
import sys
import time
import requests
from datetime import datetime
from typing import Dict, List

# Test queries
TEST_QUERIES = [
    "sdwan get all alarms",
    "sdwan get active alarms",
    "sdwan list all devices",
    "get All Device Status",
    "sdwan get device health",
    "sdwan get segment",
    "sdwan get all policies",
    "sdwan get sites",
    "sdwan get users",
    "sdwan get software version"
]

class SDWANAPITester:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.results = []
        
    def test_query(self, query: str) -> Dict:
        """Test a single query via the chat API"""
        print(f"\nTesting: {query}")
        start_time = time.time()
        
        try:
            response = requests.post(
                f"{self.base_url}/chat",
                json={"message": query},
                timeout=30
            )
            
            elapsed_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                response_text = data.get("response", "")
                
                # Try to detect which function was called by analyzing the response
                function_called = self._detect_function(query, response_text)
                
                return {
                    "query": query,
                    "status": "success",
                    "function_called": function_called,
                    "response_preview": response_text[:200] + "..." if len(response_text) > 200 else response_text,
                    "elapsed_time": elapsed_time
                }
            else:
                return {
                    "query": query,
                    "status": "failed",
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "elapsed_time": elapsed_time
                }
                
        except requests.exceptions.ConnectionError:
            return {
                "query": query,
                "status": "failed",
                "error": "Connection refused - is the server running?",
                "elapsed_time": time.time() - start_time
            }
        except Exception as e:
            return {
                "query": query,
                "status": "failed", 
                "error": str(e),
                "elapsed_time": time.time() - start_time
            }
    
    def _detect_function(self, query: str, response: str) -> str:
        """Try to detect which function was called based on query and response"""
        query_lower = query.lower()
        response_lower = response.lower()
        
        # Map queries to likely functions based on keywords
        if "alarm" in query_lower:
            if "active" in query_lower:
                return "getActiveAlarms"
            else:
                return "getRawAlarmData"
        elif "device" in query_lower:
            if "status" in query_lower:
                return "getAllDeviceStatus"
            elif "health" in query_lower:
                return "getDeviceHealthDetails"
            else:
                return "listAllDevices"
        elif "segment" in query_lower:
            return "getTransportSegmentation"
        elif "policies" in query_lower or "policy" in query_lower:
            return "getAllPoliciesV1"
        elif "site" in query_lower:
            return "getSiteHealthDetails"
        elif "user" in query_lower:
            return "findUsers_1"
        elif "software" in query_lower or "version" in query_lower:
            return "getSoftwareDistribution"
        
        return "Unknown function"
    
    def run_all_tests(self):
        """Run all test queries"""
        print("="*60)
        print("SD-WAN API Test Suite")
        print("="*60)
        print(f"Testing {len(TEST_QUERIES)} queries against {self.base_url}")
        print("="*60)
        
        # First check if server is running
        try:
            response = requests.get(f"{self.base_url}/docs", timeout=5)
            if response.status_code != 200:
                print("\n❌ Server is not responding properly!")
                print(f"   Please ensure the FastAPI server is running on {self.base_url}")
                print("   Run: python3 -m app.user_commands.start_cisco_platform_ai")
                return False
        except:
            print("\n❌ Cannot connect to server!")
            print(f"   Please ensure the FastAPI server is running on {self.base_url}")
            print("   Run: python3 -m app.user_commands.start_cisco_platform_ai")
            return False
        
        print("✅ Server is running!\n")
        
        # Run tests
        for query in TEST_QUERIES:
            result = self.test_query(query)
            self.results.append(result)
            
            # Brief status
            if result["status"] == "success":
                print(f"   ✅ Success - Function: {result['function_called']}")
            else:
                print(f"   ❌ Failed - {result.get('error', 'Unknown error')}")
        
        return True
    
    def generate_report(self):
        """Generate and save test report"""
        print("\n" + "="*60)
        print("TEST RESULTS SUMMARY")
        print("="*60)
        
        successful = [r for r in self.results if r["status"] == "success"]
        failed = [r for r in self.results if r["status"] == "failed"]
        
        print(f"\nTotal Tests: {len(self.results)}")
        print(f"Successful: {len(successful)} ✅")
        print(f"Failed: {len(failed)} ❌")
        
        if successful:
            print("\n" + "-"*60)
            print("SUCCESSFUL QUERIES:")
            print("-"*60)
            for result in successful:
                print(f"\n✅ Query: '{result['query']}'")
                print(f"   Function: {result['function_called']}")
                print(f"   Time: {result['elapsed_time']:.2f}s")
                print(f"   Response: {result['response_preview']}")
        
        if failed:
            print("\n" + "-"*60)
            print("FAILED QUERIES:")
            print("-"*60)
            for result in failed:
                print(f"\n❌ Query: '{result['query']}'")
                print(f"   Error: {result.get('error', 'Unknown error')}")
                print(f"   Time: {result['elapsed_time']:.2f}s")
        
        # Save detailed results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"sdwan_test_results_{timestamp}.json"
        
        with open(report_file, "w") as f:
            json.dump({
                "test_date": datetime.now().isoformat(),
                "server_url": self.base_url,
                "summary": {
                    "total": len(self.results),
                    "successful": len(successful),
                    "failed": len(failed)
                },
                "results": self.results
            }, f, indent=2)
        
        print(f"\n\n📄 Detailed results saved to: {report_file}")
        
        # Check environment variables
        print("\n" + "-"*60)
        print("ENVIRONMENT CHECK:")
        print("-"*60)
        required_vars = ["SDWAN_BASE_URL", "SDWAN_USERNAME", "SDWAN_PASSWORD"]
        for var in required_vars:
            value = os.getenv(var)
            if value:
                print(f"✅ {var}: Set")
            else:
                print(f"❌ {var}: Not set")
        
        return len(failed) == 0


def main():
    """Main entry point"""
    # Get server URL from command line or use default
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    
    tester = SDWANAPITester(base_url)
    
    if tester.run_all_tests():
        success = tester.generate_report()
        
        if success:
            print("\n🎉 All tests passed!")
            return 0
        else:
            print("\n⚠️  Some tests failed!")
            return 1
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
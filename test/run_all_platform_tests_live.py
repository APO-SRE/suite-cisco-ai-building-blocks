#!/usr/bin/env python3
"""
Run All Platform Tests with Live Output
Executes multiple platform test suites sequentially with real-time output
Perfect for CI/CD or scheduled testing
"""
import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime

# Define test suites to run
TEST_SUITES = [
    {
        "name": "SD-WAN Tests",
        "script": "sdwan_test_automated.py",
        "port": 8001
    },
    {
        "name": "Intersight Tests",
        "script": "intersight_test_automated.py",
        "port": 8002
    },
    {
        "name": "Meraki Tests",
        "script": "meraki_test_automated.py", 
        "port": 8003
    },
    {
        "name": "Catalyst Tests",
        "script": "catalyst_test_automated.py",
        "port": 8004
    },
]

def run_test_suite(suite: dict) -> dict:
    """Run a single test suite with live output"""
    print(f"\n{'='*60}")
    print(f"Running: {suite['name']}")
    print(f"Script: {suite['script']}")
    print(f"Port: {suite['port']}")
    print('='*60)
    
    test_dir = Path(__file__).parent
    script_path = test_dir / suite['script']
    
    if not script_path.exists():
        print(f"❌ Test script not found: {script_path}")
        return {
            "name": suite['name'],
            "status": "not_found",
            "error": f"Script {suite['script']} not found"
        }
    
    # Run the test with live output
    start_time = datetime.now()
    try:
        # Use Popen for real-time output
        process = subprocess.Popen(
            [sys.executable, str(script_path), str(suite['port'])],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,  # Line buffered
            universal_newlines=True
        )
        
        # Stream output in real-time
        output_lines = []
        for line in process.stdout:
            print(line, end='')  # Print in real-time
            output_lines.append(line)
        
        # Wait for completion
        process.wait()
        
        elapsed = (datetime.now() - start_time).total_seconds()
        full_output = ''.join(output_lines)
        
        if process.returncode == 0:
            print(f"\n✅ {suite['name']} completed successfully")
            return {
                "name": suite['name'],
                "status": "success",
                "elapsed_seconds": elapsed,
                "output": full_output
            }
        else:
            print(f"\n❌ {suite['name']} failed with exit code {process.returncode}")
            return {
                "name": suite['name'],
                "status": "failed",
                "exit_code": process.returncode,
                "elapsed_seconds": elapsed,
                "output": full_output
            }
            
    except Exception as e:
        print(f"\n❌ {suite['name']} crashed: {e}")
        return {
            "name": suite['name'],
            "status": "error",
            "error": str(e)
        }

def main():
    """Run all test suites"""
    print("🤖 Platform Test Suite Runner (Live Output)")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📊 Running {len(TEST_SUITES)} test suite(s)")
    
    # Check virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("\n⚠️  WARNING: Not running in a virtual environment")
        print("   Activate with: source ~/env/bin/activate")
    
    # Run all test suites
    results = []
    for suite in TEST_SUITES:
        result = run_test_suite(suite)
        results.append(result)
    
    # Generate summary report
    print("\n" + "="*60)
    print("SUMMARY REPORT")
    print("="*60)
    
    successful = [r for r in results if r["status"] == "success"]
    failed = [r for r in results if r["status"] in ["failed", "error"]]
    not_found = [r for r in results if r["status"] == "not_found"]
    
    print(f"Total Suites: {len(results)}")
    print(f"Successful: {len(successful)} ✅")
    print(f"Failed: {len(failed)} ❌")
    print(f"Not Found: {len(not_found)} ⚠️")
    
    if failed:
        print("\nFailed Suites:")
        for r in failed:
            print(f"  - {r['name']}: {r['status']}")
    
    # Save master report (without full output to keep file size reasonable)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = Path(__file__).parent / f"all_platforms_test_report_{timestamp}.json"
    
    # Create report with summary output only
    report_data = {
        "test_date": datetime.now().isoformat(),
        "summary": {
            "total": len(results),
            "successful": len(successful),
            "failed": len(failed),
            "not_found": len(not_found)
        },
        "results": [
            {k: v for k, v in r.items() if k != 'output'} 
            for r in results
        ]
    }
    
    with open(report_file, "w") as f:
        json.dump(report_data, f, indent=2)
    
    print(f"\n📄 Master report saved to: {report_file}")
    
    # Exit with appropriate code
    if failed or not_found:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
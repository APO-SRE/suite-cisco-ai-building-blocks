#!/usr/bin/env python3
"""
Test the IntersightClient resolve mechanism
"""

import sys
from pathlib import Path
import os

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Set dummy credentials
os.environ['INTERSIGHT_API_KEY'] = 'dummy_key'
os.environ['INTERSIGHT_API_SECRET'] = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwJuCqe5CAqlKnCCmKqOSb3pu6v7AhF3cXxzJ4YCvVJ7TUe0z
L8hLZPPinKmfDRh53x5lqZMEX6LjEOTDUmjMFgJmM+5dc6rrLDN47HQZV8hGUZw8
xV7s4x0a4CZq7pf2MJ1h9FkLNPh4gPCqxKEWgcCYqZMksWaUShQ/GZEF0QkTdgx8
LFYdMGEVYbfWWQPglBFSH/2aE6Iza6hZCVsPpQEEqLzAugR2yT2BRQFI6cXLlqgx
06xzLvVmQ7HCGEbDRXNcKv1rwHJ7oU8DbqGgmwajuyuaQPOVjpe0s3rP1M13PWUY
AzMNx5dpHDrraC6VgjKErAByJfBOEjuNPhrjgwIDAQABAoIBAE4i1lZn5BnJPGwE
qxWdWsarc5muTmSju7DQF2A5mpjdPfFZHPw0A5RU0nl8fJWU8H2RcZNmRKnK11LZ
j9wy2wZBjO8l6+bWP9ODUUwSmNdsqQkOyeQKrYqHLEKCM4JTN5nQQCimnLwG+2SL
Cr8vuNHG1KzGBCLffLgKz17vD4M37jEPxXfQlHW0G0Gu0Qzjh8meUFEFUQdVBcGy
uRb8KhLvdAgc5CjbLpCU7VvRqJFHJAVpa7IejKxWDQpoOHPxOBfrY4hXp0Ajqcxc
FJNmQwGz1dQwjJCUgfONx3HFnRfqLRCkqCLqFLXL7W2GtOmKs2TX9TdxZQ2jcCf5
UIwhYEECgYEA4mKJgaDtYRvF/4A6l7qFHwVZh8iboOCLge6YeMXqrtpDxcalLcNc
Av/0cu/H2WHM0FwnKHpZVT4xuHNKGKCv6hTuhFKLU3XMlv3S1pTTjfKDoJv8LXQK
oEBB3tie3wC7c0aHqYT5mIECRVVvJTKgQmqepFsAKNd3UWGuR+H6vIMCgYEA2mWk
p7xL1G2pW6V7pDHJqwV8z6gG8rQ2Z7QvasC42Nb1Fjge2YQPj/s3p5WivQMgXp8N
NiGUXoqBnhxQxtzLMx1uKRueq3YiZ5RcBzvtKconRuLSAoOEuLCqHpq9kFP9p7Q6
9LbF7F7TdWoEFWx8escQ5JCfWqbPV7E8rKLGjsECgYBWb+8/bFdz0gFN0kLQPxYC
8DGj8FZFYI2wYO1YoLLxTQYN8d7ranDElnJdHneCTKShEtmOVSjTZmUFDqHQNjes
TxKVUMjUc3CX6FYCL8bL2d/4UYLixCFp9TjMgWenNKTcusLqyPEjOhVOqqU5aWxf
uaHFHkQyPJDls1KDMPMMqwKBgQCCKjtHVNqGGRcV9sOj4cGBnUuf8xacYuNPnQ8K
JCm8fV3JQYT8t3mW8bhmPsLNLu9TVyUYcD6jouch2z5Y1UrHzaGlVLZeDDC8HsNE
vsKmthurZgJMOlNtE7LCYD/VmC4nU7h2PslQkShbfariU6YQVMwV6RG0Z9yvvKDg
UF2AgQKBgQCISQj8xb5LHGf4fEGg3OGyM8YoQiJmacLBRHopO9VLOLjcR2nKnD7R
W8TRBONqKKlLV7mCPFaIbk2JkMGJXKe4oFWCZ8MH8lkaBiZW/yb3lVqMHWGVSqHV
mKBfQBy5CqV4p9pAJQcOT1rKCQ8kLZF7rKiY1pE9LkfAXaC1pbvtLw==
-----END RSA PRIVATE KEY-----"""

try:
    from app.llm.platform_clients.intersight_client import IntersightClient
    import re
    
    print("Testing IntersightClient _resolve mechanism\n")
    print("=" * 60)
    
    # Test the resolve logic manually
    name = 'get_compute_physical_summary_list'
    _CAMEL_TO_SNAKE = re.compile(r'(?<!^)(?=[A-Z])')
    snake = _CAMEL_TO_SNAKE.sub('_', name).lower()
    
    print(f"Original name: {name}")
    print(f"Snake case: {snake}")
    
    # Split into parts for module detection
    parts = snake.split('_')
    print(f"Parts: {parts}")
    
    # Test what tag would be generated
    for i in range(len(parts), 0, -1):
        tag = '_'.join(parts[:i])
        module_name = f"intersight.api.{tag}_api"
        class_name = f"{''.join(p.capitalize() for p in tag.split('_'))}Api"
        print(f"\nTrying tag '{tag}':")
        print(f"  Module: {module_name}")
        print(f"  Class: {class_name}")
        
        try:
            import importlib
            mod = importlib.import_module(module_name)
            print(f"  ✓ Module exists!")
            if hasattr(mod, class_name):
                print(f"  ✓ Class {class_name} exists!")
                # Stop at first match
                break
            else:
                print(f"  ✗ Class {class_name} not found")
        except ImportError as e:
            print(f"  ✗ Module not found: {e}")
    
    # Now test the actual client
    print("\n" + "=" * 60)
    print("Testing actual IntersightClient resolution:")
    
    try:
        client = IntersightClient()
        print(f"\nAttempting to resolve: {name}")
        
        # This should trigger __getattr__ and _resolve
        method = getattr(client, name)
        print(f"✓ Successfully resolved to: {method}")
        
    except Exception as e:
        print(f"✗ Failed to resolve: {e}")
        import traceback
        traceback.print_exc()

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
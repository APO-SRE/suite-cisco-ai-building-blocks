#!/usr/bin/env python3
"""
Get Intersight Organization MOID Tool

This tool retrieves the Organization MOID(s) from Intersight using the API key
stored in the .env file. This is useful for setting the INTERSIGHT_ORGANIZATION_MOID
environment variable.

Usage:
    python tools/GetIntersightOrgMOID.py
    python tools/GetIntersightOrgMOID.py --name "My Organization"
    python tools/GetIntersightOrgMOID.py --export
"""

import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    import intersight
    from intersight.api.organization_api import OrganizationApi
    from intersight.exceptions import ApiException
except ImportError:
    print("Error: intersight SDK not found. Please install it with:")
    print("  pip install intersight")
    sys.exit(1)


def setup_intersight_client():
    """Setup Intersight client with credentials from .env file."""
    # Load environment variables from .env file
    load_dotenv()
    
    api_key = os.getenv('INTERSIGHT_API_KEY')
    api_secret = os.getenv('INTERSIGHT_API_SECRET')
    base_url = os.getenv('INTERSIGHT_BASE_URL', 'https://intersight.com')
    
    if not api_key or not api_secret:
        print("Error: Missing INTERSIGHT_API_KEY or INTERSIGHT_API_SECRET in .env file")
        print("\nPlease ensure your .env file contains:")
        print("  INTERSIGHT_API_KEY=your_api_key_here")
        print("  INTERSIGHT_API_SECRET=/path/to/secret_key.pem")
        sys.exit(1)
    
    # Resolve secret key path
    secret_path = Path(api_secret).expanduser()
    if secret_path.is_file():
        secret_content = secret_path.read_text()
    else:
        secret_content = api_secret.strip()
    
    # Determine signing algorithm
    if 'BEGIN RSA PRIVATE KEY' in secret_content:
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
    elif 'BEGIN EC PRIVATE KEY' in secret_content:
        signing_algorithm = intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
    else:
        print("Error: INTERSIGHT_API_SECRET is not a valid RSA or EC private key")
        sys.exit(1)
    
    # Configure Intersight API client
    config = intersight.Configuration(
        host=base_url,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key,
            private_key_string=secret_content,
            signing_scheme=intersight.signing.SCHEME_HS2019,
            signing_algorithm=signing_algorithm,
            hash_algorithm=intersight.signing.HASH_SHA256,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ]
        )
    )
    
    return intersight.ApiClient(config)


def get_organizations(api_client, org_name=None):
    """Get organization(s) from Intersight."""
    try:
        org_api = OrganizationApi(api_client)
        
        # Get organizations
        print(f"Fetching organizations from Intersight...")
        
        if org_name:
            # Query with filter if organization name is provided
            filter_str = f"Name eq '{org_name}'"
            response = org_api.get_organization_organization_list(filter=filter_str)
        else:
            # Query without filter to get all organizations
            response = org_api.get_organization_organization_list()
        
        return response.results
        
    except ApiException as e:
        print(f"Error calling Intersight API: {e}")
        if e.status == 401:
            print("\nAuthentication failed. Please check your API credentials.")
        elif e.status == 403:
            print("\nAccess denied. Please check your API key permissions.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def display_organizations(organizations):
    """Display organization information in a formatted table."""
    if not organizations:
        print("\nNo organizations found.")
        return None
    
    print(f"\nFound {len(organizations)} organization(s):\n")
    print(f"{'Name':<30} {'MOID':<40} {'Description':<40}")
    print("-" * 110)
    
    default_org = None
    for org in organizations:
        name = org.name
        moid = org.moid
        desc = (org.description or "No description")[:40]
        
        # Track the default organization
        if hasattr(org, 'is_default') and org.is_default:
            default_org = org
            name += " (default)"
        
        print(f"{name:<30} {moid:<40} {desc:<40}")
    
    return default_org or (organizations[0] if len(organizations) == 1 else None)


def export_to_env(org_moid, org_name):
    """Export the organization MOID to .env file."""
    env_path = Path('.env')
    
    # Read existing .env content
    if env_path.exists():
        content = env_path.read_text()
        lines = content.splitlines()
    else:
        lines = []
    
    # Check if INTERSIGHT_ORGANIZATION_MOID already exists
    updated = False
    for i, line in enumerate(lines):
        if line.startswith('INTERSIGHT_ORGANIZATION_MOID='):
            lines[i] = f'INTERSIGHT_ORGANIZATION_MOID={org_moid}'
            updated = True
            break
    
    # Add if not found
    if not updated:
        lines.append(f'INTERSIGHT_ORGANIZATION_MOID={org_moid}')
    
    # Write back to file
    env_path.write_text('\n'.join(lines) + '\n')
    
    print(f"\n✅ Exported INTERSIGHT_ORGANIZATION_MOID to .env file")
    print(f"   Organization: {org_name}")
    print(f"   MOID: {org_moid}")


def main():
    parser = argparse.ArgumentParser(
        description="Get Intersight Organization MOID(s)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all organizations
  python tools/GetIntersightOrgMOID.py
  
  # Get specific organization by name
  python tools/GetIntersightOrgMOID.py --name "My Organization"
  
  # Export organization MOID to .env file
  python tools/GetIntersightOrgMOID.py --export
  
  # Export specific organization to .env
  python tools/GetIntersightOrgMOID.py --name "My Organization" --export
"""
    )
    
    parser.add_argument(
        '--name', '-n',
        help='Filter by organization name'
    )
    parser.add_argument(
        '--export', '-e',
        action='store_true',
        help='Export organization MOID to .env file'
    )
    
    args = parser.parse_args()
    
    # Setup API client
    print("Connecting to Intersight...")
    api_client = setup_intersight_client()
    
    # Get organizations
    organizations = get_organizations(api_client, args.name)
    
    # Display organizations
    selected_org = display_organizations(organizations)
    
    # Export if requested
    if args.export:
        if not organizations:
            print("\nNo organization to export.")
        elif len(organizations) == 1 or selected_org:
            org = selected_org or organizations[0]
            export_to_env(org.moid, org.name)
        else:
            print("\nMultiple organizations found. Please specify --name to select one.")
            print("Example: python tools/GetIntersightOrgMOID.py --name 'My Organization' --export")
    else:
        if organizations:
            print("\nTo export an organization MOID to your .env file, run:")
            if len(organizations) == 1:
                print("  python tools/GetIntersightOrgMOID.py --export")
            else:
                print("  python tools/GetIntersightOrgMOID.py --name 'Organization Name' --export")


if __name__ == "__main__":
    main()
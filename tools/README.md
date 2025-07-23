# Cisco AI Building Blocks - Tools

This directory contains utility tools for working with the Cisco AI Building Blocks suite.

## Available Tools

### GetIntersightOrgMOID.py

Retrieves Intersight Organization MOIDs using your configured API credentials.

**Purpose:**
- Fetch organization MOIDs from Intersight
- Automatically export the MOID to your `.env` file
- Useful for setting up `INTERSIGHT_ORGANIZATION_MOID` environment variable

**Prerequisites:**
- Intersight API credentials in your `.env` file:
  ```
  INTERSIGHT_API_KEY=your_api_key_here
  INTERSIGHT_API_SECRET=/path/to/secret_key.pem
  ```

**Usage:**
```bash
# List all organizations
python tools/GetIntersightOrgMOID.py

# Get specific organization by name
python tools/GetIntersightOrgMOID.py --name "My Organization"

# Export organization MOID to .env file (auto-selects if only one org)
python tools/GetIntersightOrgMOID.py --export

# Export specific organization to .env
python tools/GetIntersightOrgMOID.py --name "My Organization" --export
```

**Example Output:**
```
Connecting to Intersight...
Fetching organizations from Intersight...

Found 2 organization(s):

Name                           MOID                                     Description
--------------------------------------------------------------------------------------------------------------
default (default)              5a1b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r    Default organization
My Test Organization           6b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s    Test environment

To export an organization MOID to your .env file, run:
  python tools/GetIntersightOrgMOID.py --name 'Organization Name' --export
```

**Features:**
- Automatically detects RSA or EC private keys
- Handles both file paths and inline private keys
- Shows which organization is the default
- Updates existing `.env` file without overwriting other variables
- Provides clear error messages for authentication issues
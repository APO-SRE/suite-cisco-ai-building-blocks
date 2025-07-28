# Platform Scaffolder Documentation

## Overview

The Platform Scaffolder is a critical component of the Suite Cisco AI Building Blocks that automatically generates LLM-friendly function definitions and client wrappers for Cisco platform SDKs. It processes OpenAPI specifications to create a standardized interface that allows Large Language Models (LLMs) to interact with various Cisco platforms like Meraki, Catalyst Center, Intersight, SD-WAN, and others.

## Purpose

The primary purposes of the Platform Scaffolder are:

1. **Automatic SDK Wrapper Generation** - Creates Python client wrappers that provide:
   - Unified authentication handling using environment variables
   - Dynamic method resolution (camelCase → snake_case conversion)
   - Platform-specific customizations

2. **LLM Function Schema Generation** - Generates OpenAI-compatible function schemas that:
   - Describe available operations for each platform
   - Include parameter definitions and types
   - Provide enhanced descriptions for better LLM understanding

3. **Service Abstraction** - Creates high-level service interfaces that:
   - Simplify platform access for applications
   - Provide a consistent API across different Cisco platforms
   - Handle authentication transparently

## Running the Platform Scaffolder

### Method 1: Direct Execution
```bash
cd /path/to/suite-cisco-ai-building-blocks
python3 src/scripts/platform_scaffolder.py [platform_names] [options]

# Examples:
python3 src/scripts/platform_scaffolder.py meraki
python3 src/scripts/platform_scaffolder.py catalyst intersight
python3 src/scripts/platform_scaffolder.py --drop-cache meraki catalyst
```

**Options:**
- `--include-http GET POST PUT` - Only include specific HTTP methods
- `--name-pattern "pattern"` - Filter operations by regex pattern
- `--sdk-module module_name` - Override SDK module name
- `--drop-cache` - Clear the dynamic cache before scaffolding

### Method 2: Using create_platform.py Menu
The scaffolder can also be run through the interactive menu system:
```bash
python3 src/scripts/create_platform.py
```
Select the option to scaffold platforms from the menu.

## Directory Structure

### Platform Customizations Directory
The `src/scripts/platform_customizations/` directory is where platform-specific customizations are managed without modifying core scripts:

```
src/scripts/platform_customizations/
├── __init__.py                 # Package initialization
├── platform_overrides.py       # Platform-specific overrides and configurations
├── injection_config.py         # Parameter injection configurations
├── aliases.py                  # Function alias generation logic
└── platform_auth.py           # Platform-specific authentication configurations
```

#### Key Files:

1. **platform_overrides.py** - Contains:
   - Function blocklists (operations to exclude)
   - Description overrides for better LLM understanding
   - SDK filtering configuration
   - Operation ID mappings

2. **injection_config.py** - Defines:
   - Automatic parameter injection (e.g., org_id for Meraki)
   - Environment variable mappings
   - Parameter templates

3. **platform_auth.py** - Manages:
   - Platform-specific authentication methods
   - Environment variable requirements
   - SDK initialization logic

4. **aliases.py** - Provides:
   - Function alias generation
   - Alternative naming for operations

### Utility Modules
The `src/scripts/platform_scaffolder_utilities/` directory contains reusable utility modules:

```
src/scripts/platform_scaffolder_utilities/
├── __init__.py
├── scaffolder_helpers.py       # General utility functions
├── sdk_processing.py          # SDK introspection and filtering
├── client_generator.py        # Client wrapper generation
└── unified_service_generator.py # Service interface generation
```

## Function Priorities and Weights

### Dynamic Weight Assignment
Function priorities are dynamically set in `src/app/llm/dynamic.py` during runtime. This system:
- Analyzes user queries to determine relevant functions
- Assigns weights based on relevance and context
- Optimizes function selection for LLM responses

### Manual Priority Configuration
Function priorities can be manually adjusted without modifying code by editing:
```
src/app/llm/platform_dynamic_cache/function_priorities.json
```

Example content:
```json
{
    "meraki": {
        "getOrganizations": 100,
        "getOrganizationNetworks": 90,
        "getNetworkDevices": 85
    },
    "catalyst": {
        "getAllInterfaces": 95,
        "getDeviceList": 90
    }
}
```

Higher values indicate higher priority for function selection.

## Generated Artifacts

The scaffolder generates several types of files:

1. **Function Schemas** (`src/app/llm/platform_function_schemas/`)
   - `{platform}_functions.json` - OpenAI-compatible function definitions

2. **Client Wrappers** (`src/app/llm/cisco_clients/`)
   - `{platform}_client.py` - Python client with auth handling

3. **Service Interfaces** (`src/app/llm/cisco/`)
   - `{platform}/__init__.py` - High-level service wrapper

4. **Dynamic Cache** (`src/app/llm/platform_dynamic_cache/`)
   - `full_schemas.json` - Consolidated function schemas
   - `function_priorities.json` - Function priority configuration

## Customization Guide

### Adding a New Platform
1. Add platform configuration to `platform_overrides.py`
2. Add authentication logic to `platform_auth.py`
3. Add parameter injection rules to `injection_config.py` (if needed)
4. Run the scaffolder for the new platform

### Modifying Platform Behavior
1. **Block Functions**: Add operation IDs to the blocklist in `platform_overrides.py`
2. **Enhance Descriptions**: Add description overrides in `platform_overrides.py`
3. **Adjust Priorities**: Edit `function_priorities.json`
4. **Change Auth**: Update logic in `platform_auth.py`


## Best Practices

1. **Always test** after making customizations
2. **Use environment variables** for sensitive configuration
3. **Document** any platform-specific quirks in comments
4. **Follow naming conventions** for consistency
5. **Run with --drop-cache** when making structural changes

## Troubleshooting

Common issues and solutions:

1. **Missing SDK Module**: Ensure the platform SDK is installed
2. **Auth Failures**: Check environment variables are set correctly
3. **Function Not Found**: Verify operation ID in OpenAPI spec
4. **Import Errors**: Ensure Python path includes project root

For additional help, check the logs or run with increased verbosity.
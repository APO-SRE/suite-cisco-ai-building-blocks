#!/usr/bin/env python3

import shutil
import os

# List of folders you want to delete and recreate
folders_to_reset = [
    "app/llm/function_definitions",
    "app/llm/openapi_specs",
    "app/llm/platform_clients",
    "app/llm/function_dispatcher",
    "app/llm/unified_service"
]

def reset_folders(folder_paths):
    for folder in folder_paths:
        # Delete the folder if it exists
        if os.path.exists(folder):
            print(f"Deleting folder: {folder}")
            shutil.rmtree(folder)
        else:
            print(f"Folder not found (skipped delete): {folder}")

        # Recreate the empty folder
        print(f"Recreating folder: {folder}")
        os.makedirs(folder, exist_ok=True)

if __name__ == "__main__":
    reset_folders(folders_to_reset)
    print("All specified folders have been reset.")

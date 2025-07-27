# tools/explore_local_sdk.py (Version 3 - With Debugging and Cycle Detection)
# This script inspects the locally installed catalystwan library.
# It includes verbose logging and protection against infinite loops.

import logging
from types import ModuleType
from typing import Set
from catalystwan.session import ManagerSession
from catalystwan.vmanage_auth import vManageAuth
from rich.console import Console
from rich.tree import Tree

# --- Configuration ---
console = Console()
# Suppress the "No credentials provided" warning, as it's expected.
logging.disable(logging.WARNING)


def explore_sdk_tree(obj: object, tree_node: Tree, visited_ids: Set[int], path_prefix: str = ""):
    """
    Recursively explores an object to build a Rich Tree of its attributes and methods.
    Includes cycle detection to prevent infinite loops.

    Args:
        obj: The Python object to explore.
        tree_node: The rich.tree.Tree branch to add new items to.
        visited_ids: A set of IDs of objects already visited to prevent cycles.
        path_prefix: The current dot-notation path for logging.
    """
    # --- FIX: CYCLE DETECTION ---
    # If we have already processed this exact object, stop here to prevent an infinite loop.
    if id(obj) in visited_ids:
        return
    # Mark this object as visited.
    visited_ids.add(id(obj))

    public_attrs = sorted([attr for attr in dir(obj) if not attr.startswith('_')])

    for attr_name in public_attrs:
        try:
            child_obj = getattr(obj, attr_name)
            current_path = f"{path_prefix}.{attr_name}" if path_prefix else attr_name

            # --- DEBUG: Log the current attribute being processed ---
            console.log(f"Processing: {current_path}")

            # Skip modules and other uninteresting built-ins
            if isinstance(child_obj, ModuleType) or attr_name in ['mro', 'model_config', 'parent', 'root']:
                continue

            # If the attribute is another object (a sub-API), create a new branch and recurse
            if hasattr(child_obj, '__dict__') and not callable(child_obj):
                branch = tree_node.add(f"📦 [bold blue]{attr_name}[/bold blue]")
                # Pass the visited_ids set down to the next level of recursion
                explore_sdk_tree(child_obj, branch, visited_ids, path_prefix=current_path)
            # If the attribute is callable (i.e., a method), display it as a leaf
            elif callable(child_obj):
                tree_node.add(f"🔧 [green]{attr_name}()[/green]  (Path: [cyan]session.api.{current_path}[/cyan])")

        except Exception:
            continue


def main():
    """
    Creates a dummy, uninitialized ManagerSession to inspect the SDK's API structure locally.
    """
    console.print("⚡️ [bold]Inspecting the locally installed `catalystwan` SDK...[/bold]")

    try:
        dummy_auth = vManageAuth(username="", password="")
        session = ManagerSession(base_url="dummy_url", auth=dummy_auth)

        console.print("✅ Successfully created a dummy session object for inspection.")

        console.print("\n" + "="*60)
        console.print("  CATALYSTWAN SDK - LOCAL API ENDPOINT TREE  ".center(60))
        console.print("="*60 + "\n")

        # This set will store the IDs of objects we've already seen.
        visited_object_ids = set()
        
        tree = Tree("session.api", guide_style="bold bright_blue")
        # Start the exploration, passing the empty set to track visited objects.
        explore_sdk_tree(session.api, tree, visited_object_ids, path_prefix="api")
        
        console.print(tree)

    except Exception as e:
        console.print(f"\n❌ [bold red]An unexpected error occurred:[/bold red] {e}")
        import traceback
        traceback.print_exc()
    finally:
        console.print("\n✅ Inspection complete. No network connection was used.")


if __name__ == "__main__":
    main()
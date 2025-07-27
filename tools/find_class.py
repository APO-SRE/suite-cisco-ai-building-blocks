# tools/find_class.py
import inspect
import catalystwan
from rich.console import Console

console = Console()

def find_the_class():
    """
    Inspects the catalystwan library to find the correct import path for ManagerSession.
    """
    console.print("\n" + "="*50)
    console.print("  Inspecting the [bold cyan]catalystwan[/bold cyan] library...  ")
    console.print("="*50)

    found_path = None
    
    # Iterate through all the modules within the catalystwan package
    for name, module in inspect.getmembers(catalystwan, inspect.ismodule):
        # Check if the ManagerSession class exists in this module
        if hasattr(module, 'ManagerSession'):
            found_path = f"from {module.__name__} import ManagerSession"
            break

    if found_path:
        console.print("\n✅ [bold green]Found it![/bold green]")
        console.print("The correct import statement for your version is:")
        console.print(f"\n[bold yellow]{found_path}[/bold yellow]\n")
    else:
        console.print("\n❌ [bold red]Could not find ManagerSession class.[/bold red]")
        console.print("This is highly unusual. Please check your catalystwan installation.")

if __name__ == "__main__":
    find_the_class()
    
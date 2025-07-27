# tools/inspect_function.py
import inspect
from catalystwan.session import create_manager_session
from rich.console import Console
from rich.panel import Panel

console = Console()

def inspect_the_function():
    """
    Inspects the create_manager_session function from the installed catalystwan
    library and prints its official signature and documentation.
    """
    try:
        console.print("\n" + "="*50)
        console.print("  Inspecting: [bold cyan]catalystwan.session.create_manager_session[/bold cyan]  ")
        console.print("="*50)

        # Get the signature of the function
        sig = inspect.signature(create_manager_session)
        
        # Get the docstring
        doc = inspect.getdoc(create_manager_session)

        console.print("\n[bold green]Function Signature:[/bold green]")
        console.print(f"[yellow]create_manager_session{sig}[/yellow]")
        
        console.print("\n[bold green]Official Documentation (Docstring):[/bold green]")
        if doc:
            console.print(Panel(doc, border_style="blue"))
        else:
            console.print("[red]No docstring found.[/red]")

    except Exception as e:
        console.print(f"\n❌ An unexpected error occurred during inspection: {e}")

if __name__ == "__main__":
    inspect_the_function()
    
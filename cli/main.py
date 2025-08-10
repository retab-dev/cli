import typer
from typing import Optional
from cli.commands.extract import extract_app

app = typer.Typer(
    help="Retab is a powerful tab management and organization tool.",
    add_completion=False,
    no_args_is_help=False
)

app.add_typer(extract_app, name="extract")

def show_welcome():
    """Display the main help message in Bun-style format"""
    version = "0.0.1"
    
    welcome_text = f"""Retab is a powerful tab management and organization tool. ({version})

Usage: retab <command> [...flags] [...args]

Commands:
  extract   create <username>      Create a new user extraction
            delete <username>      Delete a user extraction
  
  hello     <name>                 Say hello to NAME
  
  <command> --help                 Print help text for command.

Learn more about Retab:           https://github.com/your-org/retab
Report issues:                    https://github.com/your-org/retab/issues"""
    
    typer.echo(welcome_text)

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(None, "--version", "-v", help="Show version information"),
):
    """
    Retab - A powerful tab management and organization tool.
    """
    if version:
        typer.echo("retab version 0.0.1")
        return
    
    if ctx.invoked_subcommand is None:
        show_welcome()

@app.command()
def hello(name: str, count: int = 1):
    """
    Say hello to NAME, optionally multiple times.
    """
    for _ in range(count):
        typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()

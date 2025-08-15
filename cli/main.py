import typer
from typing import Optional
from cli.commands.extract import extract_app
from cli.commands.parse import parse_app
from cli.commands.mcp import mcp_app
version = "0.0.1"

app = typer.Typer(
    help="Retab is a powerful document extraction tool.",
    add_completion=False,
    no_args_is_help=False
)

app.add_typer(extract_app)
app.add_typer(parse_app)
app.add_typer(mcp_app)

def show_welcome():
    """Display the main help message in Bun-style format"""
    
    welcome_text = f"""Retab is a powerful document extraction tool. ({version})

Usage: retab <command> [...flags] [...args]

Commands:
  extract <filename> [-o <out_file>]     Extract data from a document
  parse <filename> [-o <out_file>]       Parse a document
  mcp                                    Show MCP configuration for mcp.json
  <command> --help                       Print help text for command.

Learn more about Retab:           https://github.com/your-org/retab
Report issues:                    https://github.com/your-org/retab/issues"""
    
    typer.echo(welcome_text)

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(None, "--version", "-v", help="Show version information"),
):
    if version:
        typer.echo(f"retab version {version}")
        return
    
    if ctx.invoked_subcommand is None:
        show_welcome()

if __name__ == "__main__":
    app()

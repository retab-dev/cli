# mcp.py
import typer
import json
from typing import Optional

mcp_app = typer.Typer(help="Show MCP server configuration for adding to mcp.json")

@mcp_app.command()
def mcp(
    format: Optional[str] = typer.Option("text", "--format", "-f", help="Output format: text or json")
):
    """Display MCP server configuration for Retab to add to your mcp.json file."""
    
    # Proper MCP client configuration format
    mcp_config = {
        "mcpServers": {
            "retab": {
                "url": "https://docs.retab.com/mcp",
            }
        }
    }

    server_info = {
        "description": "Plug this into your mcp.json file to use Retab's documentation in your IDE",
    }
    
    if format and format.lower() == "json":
        typer.echo("# Add this configuration to your mcp.json file:")
        typer.echo(json.dumps(mcp_config, indent=2))
    else:
        typer.echo("Retab MCP Server Configuration:")
        typer.echo("=" * 35)
        typer.echo(f"Description: {server_info['description']}")
        typer.echo("\n" + "=" * 50)
        typer.echo("MCP.JSON CONFIGURATION:")
        typer.echo("=" * 50)
        typer.echo("Add this to your mcp.json file:")
        typer.echo()
        typer.echo(json.dumps(mcp_config, indent=2))
        typer.echo()

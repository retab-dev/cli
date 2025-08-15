# mcp.py
import typer
import json
from typing import Optional

mcp_app = typer.Typer(help="Give details about the MCP server")

@mcp_app.command()
def mcp(
    format: Optional[str] = typer.Option("text", "--format", "-f", help="Output format: text or json")
):
    """Display MCP server configuration details for Retab."""
    
    mcp_config = {
        "mcpServers": {
            "retab": {
                "url": "https://docs.retab.com/mcp",
                "description": "Retab MCP Server for document extraction and parsing",
                "capabilities": [
                    "document_extraction",
                    "document_parsing", 
                    "format_conversion"
                ]
            }
        }
    }
    
    if format and format.lower() == "json":
        typer.echo(json.dumps(mcp_config, indent=2))
    else:
        typer.echo("Retab MCP Server Configuration:")
        typer.echo("=" * 35)
        typer.echo(f"URL: {mcp_config['mcpServers']['retab']['url']}")
        typer.echo(f"Description: {mcp_config['mcpServers']['retab']['description']}")
        typer.echo("Capabilities:")
        for capability in mcp_config['mcpServers']['retab']['capabilities']:
            typer.echo(f"  • {capability}")
        typer.echo("\nTo use this MCP server, add the above configuration to your MCP client.")

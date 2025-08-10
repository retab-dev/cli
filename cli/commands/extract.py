# extract.py
import typer

extract_app = typer.Typer(help="Extract and manage user data")

@extract_app.command()
def create(username: str):
    """Create a new user extraction"""
    typer.echo(f"User {username} created!")

@extract_app.command()
def delete(username: str):
    """Delete a user extraction"""
    typer.echo(f"User {username} deleted!")

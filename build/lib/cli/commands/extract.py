# extract.py
import typer

extract_app = typer.Typer()

@extract_app.command()
def create(username: str):
    typer.echo(f"User {username} created!")

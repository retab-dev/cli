import typer
from commands.extract import extract_app
app = typer.Typer()

@app.command()
def hello(name: str, count: int = 1):
    """
    Say hello to NAME, optionally multiple times.
    """
    for _ in range(count):
        typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()

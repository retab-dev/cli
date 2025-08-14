# extract.py
import typer
from typing import Annotated
import os
import sys
from cli.config import get_retab

parse_app = typer.Typer(help="Parse documents in an LLM-friendly format")

@parse_app.command()
def parse(
    filename: str,
    model: Annotated[
        str,
        typer.Option(
            "--model", "-m",
            help="Model to use for parsing",
        )
    ] = "gemini-2.5-flash",
    output: Annotated[
        str | None,
        typer.Option(
            "--output", "-o",
            help="Output file for extracted data",
            show_default="stdout"
        )
    ] = None,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite", "-w",
            help="Overwrite existing output file if it exists already",
            is_flag=True
        )
    ] = False,
):
    # stdout by default
    out_stream = sys.stdout
    if output is not None:
        if os.path.exists(output):
            if not overwrite:
                typer.echo(f"Output file {output} already exists. Use -w/--overwrite to force overwrite.")
                raise typer.Exit(code=1)
        out_stream = open(output, 'w')

    res = get_retab().documents.parse(
        document=filename,
        model=model,
    )

    out_stream.write(res.text)



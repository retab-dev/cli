# extract.py
import typer
from typing import Annotated
import os
import sys
from cli.config import get_retab

extract_app = typer.Typer(help="Extract information from documents")

@extract_app.command()
def extract(
    filename: str,
    project: Annotated[
        str | None,
        typer.Option(
            "--project", "-p",
            help="Project to use for extraction",
            show_default="<env variable RETAB_PROJECT>"
        )
    ] = None,
    iteration: Annotated[
        str | None,
        typer.Option(
            "--iteration", "-i",
            help="Iteration of the project to use for extraction",
            show_default="latest"
        )
    ] = None,
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

    if project is None:
        project = os.getenv("RETAB_PROJECT", None)
        if project is None:
            typer.echo("No project specified. Use -p/--project or set the RETAB_PROJECT environment variable.")
            raise typer.Exit(code=1)
    
    if iteration is None:
        iteration = os.getenv("RETAB_ITERATION", None)

    res = get_retab().deployments.extract(
        project_id=project,
        iteration_id=iteration,
        document=filename,
    )

    out_stream.write(res.choices[0].message.content)



"""This module provides the League App CLI."""
from typing import Optional
import typer
import os


from pathlib import Path
 
from . import __app_name__, __version__
from .league import League

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def load(inputfile: str, outputfile: str) -> None: 
    """Generate Match Score Ranking Output"""
    # CHECK IF FILES ARE VALID
    if not Path(inputfile).exists():
        typer.echo("{file} does not exists, exiting".format(file=inputfile));
        return
    if Path(outputfile).exists():
        typer.echo("{file} already exists, exiting".format(file=outputfile));
        return
    league = League()
    league.loadFile(inputfile)
    league.sort_scoreboard() # Sorted the score board
    scoreboard = league.get_scoreboard() # Get Scoreboard String 
    with open(outputfile, 'w+') as f: # Write to output file
        f.write(scoreboard)
    typer.echo("Processing Completed");
    typer.echo("Output written to {file}".format(file=outputfile));
    typer.echo("Exiting");

@app.command()
def test() -> None: 
    """Run Unit Testing"""
    os.system("python -m pytest tests/")
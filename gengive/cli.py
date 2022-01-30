#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Commandline API gateway for turvallisuusneuvonta."""
import sys
from typing import List, Union

import typer

import gengive
import gengive.gengive as gg

APP_NAME = 'Render text (Danish: gengive tekst).'
APP_ALIAS = 'gengive'
app = typer.Typer(
    add_completion=False,
    context_settings={'help_option_names': ['-h', '--help']},
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def callback(
    version: bool = typer.Option(
        False,
        '-V',
        '--version',
        help='Display the gengive version and exit',
        is_eager=True,
    )
) -> None:
    """
    Render text (Danish: gengive tekst).
    """
    if version:
        typer.echo(f'{APP_NAME} version {gengive.__version__}')
        raise typer.Exit()


@app.command('render')
def render(
    manuscript: str = typer.Option(
        '',
        '-m',
        '--manuscript',
        help='Path to input manuscript folder',
        metavar='<sourcepath>',
    ),
    target: str = typer.Option(
        '',
        '-t',
        '--target',
        help='Target (default is default)',
        metavar='target',
    ),
) -> int:
    """
    render the manuscript for target.
    """
    command = 'render'
    target = target if target else gg.DEFAULT_TARGET
    action = [command, manuscript, target]
    return sys.exit(gg.main(action))


@app.command('verify')
def verify(
    manuscript: str = typer.Option(
        '',
        '-m',
        '--manuscript',
        help='Path to input manuscript folder',
        metavar='<sourcepath>',
    ),
    target: str = typer.Option(
        '',
        '-t',
        '--target',
        help='Target (default is default)',
        metavar='target',
    ),
) -> int:
    """
    verify the request.
    """
    command = 'verify'
    target = target if target else gg.DEFAULT_TARGET
    action = [command, manuscript, target]
    return sys.exit(gg.main(action))


@app.command('version')
def app_version() -> None:
    """
    Display the gengive version and exit
    """
    callback(True)


# pylint: disable=expression-not-assigned
# @app.command()
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return gg.main(argv)

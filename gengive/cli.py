#! /usr/bin/env python3
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
    source: str = typer.Argument(''),
    manuscript: str = typer.Option(
        '',
        '-m',
        '--manuscript',
        help='Path to or name of input manuscript folder (no default)',
        metavar='<manuscript>',
    ),
    target: str = typer.Option(
        'default',
        '-t',
        '--target',
        help='Target facet to render manuscript as (default is default)',
        metavar='target',
    ),
    publisher_root: str = typer.Option(
        str(gg.PUBLISHER_ROOT),
        '-p',
        '--publisher-root',
        help=f'Publisher root (default is {gg.PUBLISHER_ROOT})',
        metavar='target',
    ),
    render_root: str = typer.Option(
        str(gg.PUBLISHER_ROOT),
        '-r',
        '--render-root',
        help=f'Render root (default is {gg.RENDER_ROOT})',
        metavar='target',
    ),
    verify: bool = typer.Option(
        False,
        '-n',
        '--dry-run',
        help='Dry run (default is False)',
    ),
) -> int:
    """
    render the manuscript for target.
    """
    command = 'render' if not verify else 'verify'
    manuscript = manuscript if manuscript else source
    target = target if target else gg.DEFAULT_TARGET
    action = [command, publisher_root, manuscript, target, render_root]
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

import click
from typing import Union

def format_help(
    obj: Union[click.Command, click.Group],
    ctx: click.Context,
    formatter: click.HelpFormatter
) -> None:
    print(obj)


def format_error(ex: click.ClickException):
    click.get
    click.echo(click.style('Error: ', fg='red') + ex.message)


def abort_error():
    print("ABORT")

import click
import importlib.metadata
import pprint as pp
from cli.app import App
from cli.command import Command

__version__ = importlib.metadata.version("etl-cli")


@click.group(cls=App)
@click.pass_context
@click.version_option(__version__, '-V', '--version', prog_name="ETL CLI Toolbox")
@click.help_option('-h', '--help')
def cli(ctx):
    pp.pprint(type(ctx))


@click.command(name='load', cls=Command)
@click.argument("file_name", type=str)
def load_file(file_name):
    click.echo("Loading file")


cli.add_command(load_file)

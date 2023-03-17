#
# (C) Eithery Lab 2023
# The main CLI application entry point
# Defines available CLI application commands and options
#
import cli
import click
from cli.app import App


@click.group(cls=App)
@click.pass_context
@click.version_option(cli.__version__, '-v', '--version', prog_name=cli.APP_DISPLAY_NAME)
@click.help_option('-h', '--help')
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command(name='load', help='Load files corresponding to the given template')
@click.argument('files', nargs=-1, required=False)
@click.option('-t', '--template')
@click.help_option('-h', '--help')
def load_files(files, template):
    click.echo(f"Loading files '{files}' with template '{template}'")

import click
from cli import __version__
from cli.app import App


@click.group(cls=App)
@click.pass_context
@click.version_option(__version__, '-V', '--version', prog_name="ETL CLI Toolbox")
@click.help_option('-h', '--help')
def cli(ctx):
    ctx.ensure_object(dict)


@cli.command(name='load', help='Loads file(s)')
@click.argument('file_name', type=str)
@click.help_option('-h', '--help')
def load_file(file_name):
    click.echo(f"Loading file '{file_name}'")

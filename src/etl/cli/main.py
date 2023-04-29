#
# (C) Eithery Lab, 2023
# The main CLI application entry point
# Defines available CLI application commands and options
#
import click
import etl.cli as cli
import etl.pipeline
from etl.cli.app import App


@click.group(cls=App)                   # type: ignore[misc]
@click.pass_context                     # type: ignore[misc]
@click.version_option(cli.__version__, '-V', '--version', prog_name=cli.APP_DISPLAY_NAME) # type: ignore[misc]
@click.help_option('-h', '--help')      # type: ignore[misc]
def main(ctx: click.Context) -> None:
    ctx.ensure_object(dict)


@main.command(name='load', help='Load files belong to the given template.') # type: ignore[misc]
@click.argument('files', nargs=-1, required=False)                          # type: ignore[misc]
@click.option('-t', '--template', metavar='TEMPLATE_NAME',                  # type: ignore[misc]
    help='Template applied to the file(s) being loaded.')
@click.option('-c', '--config', metavar='CONFIG_PATH',                      # type: ignore[misc]
    help='Path to the custom app configuration file.')
@click.option('-v', '--verbose', type=bool, is_flag=True, default=False,    # type: ignore[misc]
    help='Verbose mode. Display additional details.')
@click.help_option('-h', '--help')                                          # type: ignore[misc]
def load_files(files: tuple[str, ...], template: str, config: str, verbose: bool) -> None:
    print('Files:', files)
    print('Template', template)
    etl.pipeline.run(files, template, config, verbose)

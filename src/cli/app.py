import sys
import click
from cli import __version__


class App(click.Group):
    group_class = type

    def main(self, *args, **kwargs):
        try:
            super().main(*args, standalone_mode=False, **kwargs)
        except click.ClickException as e:
            self.format_error(e)
            sys.exit(e.exit_code)
        except click.exceptions.Abort:
            display_message('Aborted!')
            sys.exit(1)


    def format_help(self, ctx: click.Context, formatter: click.HelpFormatter):
        click.secho(f'ETL CLI Toolbox, version {__version__}\n', fg='bright_cyan')
        super().format_help(ctx, formatter)


    def format_error(self, ex: click.ClickException):
        display_message('Error: ' + str(ex))


def display_message(message: str):
    click.secho(message, fg='bright_red')

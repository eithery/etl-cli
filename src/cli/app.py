#
# (C) Eithery Lab 2023
# Defines CLI application class
# Overrides CLI error handling and help formatting
#
import cli
import click
import sys


class App(click.Group):
    group_class = type

    def main(self, *args, **kwargs):
        try:
            super().main(*args, standalone_mode=False, **kwargs)
        except click.ClickException as e:
            cli.error(str(e))
            sys.exit(e.exit_code)
        except click.exceptions.Abort:
            cli.error('Aborted!', prefix=None)
            sys.exit(1)


    def format_help(self, ctx: click.Context, formatter: click.HelpFormatter):
        click.secho(f'{cli.APP_DISPLAY_NAME}, version {cli.__version__}\n', fg='bright_cyan')
        return super().format_help(ctx, formatter)

import sys
import click
from cli.cli import format_error, abort_error, format_help

class Command(click.Command):
    standalone_mode = False

    def main(self, *args, standalone_mode: bool=True, **kwargs):
        try:
            result = super().main(*args, standalone_mode=False, **kwargs)
            if not standalone_mode:
                return result
        except click.ClickException as e:
            if not standalone_mode:
                raise
            format_error(e)
            sys.exit(e.exit_code)
        except click.exceptions.Abort:
            if not standalone_mode:
                raise
            abort_error()
            sys.exit(1)


    def format_help(self, ctx: click.Context, formatter: click.HelpFormatter):
        print(self)
        super().format_help(ctx, formatter)

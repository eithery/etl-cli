#
# (C) Eithery Lab, 2023
# CLI package level primitives
# Provides the app version and service functions for stdout/stderr colorful output
#
import click
import importlib.metadata

_ERROR_COLOR = 'red'
_WARNING_COLOR = 'yellow'
_SUCCESS_COLOR = 'green'

APP_DISPLAY_NAME = 'ETL CLI Toolbox'

__version__ = importlib.metadata.version('etl-cli')


def error(message: str, prefix: str='Error:'):
    _display_message(message, prefix, color=_ERROR_COLOR)


def warning(message: str, prefix: str='Warning:'):
    _display_message(message, prefix, color=_WARNING_COLOR)


def success(message: str, prefix: str=None):
    _display_message(message, prefix, color=_SUCCESS_COLOR)


# private

def _display_message(message: str, prefix: str, color: str):
    combined_message = ' '.join(filter(None, [prefix, message]))
    click.secho(combined_message, fg=color)

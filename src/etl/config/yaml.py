#
# (C) Eithery Lab, 2023
# YAML configuration module
# Supports reading configuration from YAML files
#
import yaml
import etl.cli as cli
from pathlib import Path
from etl.std.result import Result, Ok, Err


def load(file_path: Path, verbose: bool=False) -> Result[dict[str, str], str]:
    if file_path.is_file():
        with open(file_path) as infile:
            result = yaml.load(infile, Loader=yaml.FullLoader) or {}
            if verbose:
                cli.echo(f"'{file_path.absolute()}' LOADED")
            return Ok(result)

    return Err(f"The file '{file_path}' doesn't exist")

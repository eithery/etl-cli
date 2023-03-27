#
# (C) Eithery Lab, 2023
# ETL pipeline module
# Implements a pipeline for ETL process
#
from pathlib import Path
from etl.config import load_config
from etl.std.result import Result, Ok


def run(files: tuple[str, ...], template: str) -> Result:
    config = load_config()
    print(f'Files: {files}, template: {template}')
    return Ok()


def _lookup_app_config() -> Path:
    pass


def _extract(files):
    pass


def _prestaging(raw_data) -> Result:
    pass


def _split():
    pass


def _parse():
    pass


class Pipeline:
    def prestaging(self):
        return self

    
    def split(self):
        return self


    def parse(self):
        return self

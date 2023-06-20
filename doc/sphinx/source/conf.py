import os
from importlib import metadata

project = 'etl-toolkit'
copyright = '2023, Eithery'
author = 'eithery'
PACKAGE_VERSION = metadata.version('etl-toolkit')
version = PACKAGE_VERSION
release = PACKAGE_VERSION

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints"
]

templates_path = ['templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['static']


if os.environ.get('READTHEDOCS') == 'True':
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
    PACKAGE_ROOT = PROJECT_ROOT.joinpath('src', 'etl')

    def run_apidoc(_):
        from sphinx.ext import apidoc

        apidoc.main([
            '--force',
            '--implicit-namespaces',
            '--module-first',
            '--separate',
            '-o',
            str(PROJECT_ROOT.joinpath('doc', 'sphinx', 'source', 'reference')),
            str(PACKAGE_ROOT)
        ])


    def setup(app):
        app.connect('builder-inited', run_apidoc)

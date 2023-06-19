from importlib import metadata

project = 'etl-toolkit'
copyright = '2023, eithery'
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

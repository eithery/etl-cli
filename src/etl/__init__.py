from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent.parent
CONFIG_DIR = ROOT_DIR.joinpath('config')
TEMPLATES_DIR = CONFIG_DIR.joinpath('templates')

# dagster-test/src/project_a/definitions.py
from dagster import definitions, load_from_defs_folder
from pathlib import Path

@definitions
def defs():
    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
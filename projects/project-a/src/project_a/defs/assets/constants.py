# dagster-test/projects/project-a/src/project_a/defs/assets/constants.py
from pathlib import Path

# WORKSPACE_ROOT is dagster-test folder
WORKSPACE_ROOT = Path(__file__).resolve().parents[6]

# PROJECT_ROOT is project-a
PROJECT_ROOT = Path(__file__).resolve().parents[4]

# DATA_DIR is the "data" folder at project root
DATA_DIR = PROJECT_ROOT / "data"

# RAW_DATA folder
RAW_DATA = PROJECT_ROOT / "data" / "raw"

# STAGE_DATA folder
STAGE_DATA = PROJECT_ROOT / "data" / "staging"

# REQUESTS_DATA folder
REQUESTS_DATA = PROJECT_ROOT / "data" / "requests"

# OUTPUT_DATA folder
OUTPUT_DATA_FILE = str(PROJECT_ROOT / "data/outputs/{}.csv")
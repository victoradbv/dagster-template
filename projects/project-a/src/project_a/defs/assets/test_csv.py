import pandas as pd
import dagster as dg
from .constants import RAW_DATA
import os
from pathlib import Path

@dg.asset(
    group_name="batch"
)
def test_csv() -> dg.MaterializeResult:
    """An example asset that creates a CSV file in the data directory."""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

    file_path = os.path.join(RAW_DATA, "test_csv.csv")

    df.to_csv(file_path, index=False)

    num_rows = len(df)

    return dg.MaterializeResult(
        metadata={
            'Number of records': dg.MetadataValue.int(num_rows)
        }
    )
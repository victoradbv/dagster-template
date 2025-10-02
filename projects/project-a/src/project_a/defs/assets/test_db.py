import requests
from dagster_duckdb import DuckDBResource
from project_a.defs.assets import constants
import dagster as dg
import os

# src/dagster_essentials/defs/assets/trips.py
@dg.asset(
    deps=["test_csv"], group_name="batch"
)
def test_db(database: DuckDBResource) -> None:
    """
      Testing db connection.
    """

    csv_path = os.path.join(constants.RAW_DATA, "test_csv.csv")   

    query = f"""
        create or replace table trips as (
          select *
          from '{csv_path}'
        );
    """

    with database.get_connection() as conn:
        conn.execute(query)
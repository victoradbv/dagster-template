import dagster as dg
from dagster_duckdb import DuckDBResource

from project_a.defs.assets import constants

class AdhocRequestConfig(dg.Config):
    filename: str
    borough: str
    start_date: str
    end_date: str

@dg.asset(
    deps=["test_csv", "test_db"], group_name="api_requests"
)

def adhoc_request(config: AdhocRequestConfig, database: DuckDBResource) -> None:
    """
      The response to an request made in the `requests` directory.
      See `requests/README.md` for more information.
    """

    # strip the file extension from the filename, and use it as the output filename
    file_path = constants.OUTPUT_DATA_FILE.format(config.filename.split('.')[0])

    # count the number of trips that picked up in a given borough, aggregated by time of day and hour of day
    query = f"""
        select *
        from trips
    """

    with database.get_connection() as conn:
        results = conn.execute(query).fetch_df()

    results.to_csv(file_path, index=False)
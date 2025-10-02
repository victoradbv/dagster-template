import dagster as dg

test_db = dg.AssetSelection.assets(["test_db"])

weekly_update_job = dg.define_asset_job(
    name="weekly_update_job",
    selection=test_db,
)

adhoc_request = dg.AssetSelection.assets(["adhoc_request"])

adhoc_request_job = dg.define_asset_job(
    name="adhoc_request_job",
    selection=adhoc_request,
)
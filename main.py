from etl.extract import extract_top_posts
from etl.transform import transform_data
from etl.load import load_to_bigquery
from google.cloud import bigquery
from google.api_core.exceptions import NotFound

def fetch_existing_ids(table_id: str) -> set:
    client = bigquery.Client()
    try:
        # Check if the table exists
        client.get_table(table_id)
        query = f"SELECT id FROM `{table_id}`"
        results = client.query(query).result()
        return set(row.id for row in results)
    except NotFound:
        print(f"Table {table_id} does not exist yet. Returning empty ID set.")
        return set()

if __name__ == "__main__":
    df_raw = extract_top_posts(subreddit_name='technology', limit=15)
    df_transformed = transform_data(df_raw)

    # Deduplicate
    existing_ids = fetch_existing_ids("reddit-etl-465703.reddit_etl.daily_posts")
    df_filtered = df_transformed[~df_transformed["id"].isin(existing_ids)]

    print(df_filtered.head())

    if not df_filtered.empty:
        load_to_bigquery(df_filtered, "reddit-etl-465703.reddit_etl.daily_posts")
    else:
        print("No new posts to upload.")
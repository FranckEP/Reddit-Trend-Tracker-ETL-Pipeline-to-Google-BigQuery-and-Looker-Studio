from google.cloud import bigquery
import pandas as pd

def load_to_bigquery(df: pd.DataFrame, table_id: str):
    """
    Loads a pandas DataFrame into a BigQuery table.
    Assumes credentials are set via environment variable.
    """
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        autodetect=True
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Wait for job to finish

    print(f"Loaded {df.shape[0]} rows to {table_id}")

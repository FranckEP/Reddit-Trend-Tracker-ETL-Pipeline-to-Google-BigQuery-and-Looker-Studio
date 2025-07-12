import pandas as pd
from datetime import datetime

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Convert UNIX timestamp to datetime
    df['created_at'] = pd.to_datetime(df['created_utc'], unit='s')

    # Truncate long text fields (optional)
    df['title'] = df['title'].str.slice(0, 250)
    df['selftext'] = df['selftext'].str.slice(0, 500)

    # Add ETL load timestamp
    df['load_date'] = datetime.utcnow()

    # Reorder / drop unnecessary columns
    df = df[[
        'id', 'title', 'score', 'num_comments',
        'author', 'subreddit', 'created_at',
        'url', 'selftext', 'load_date'
    ]]

    return df

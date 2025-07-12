# 🔧 Setup & Configuration Guide

This document describes how to set up API credentials, configure your environment, and create the required BigQuery table for the Reddit Daily Trends ETL project.

---

## 1. 🗝️ Reddit API Key Setup

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click on **"Create App"**
3. Fill in:
   - Name: `Reddit ETL`
   - Type: `script`
   - Redirect URI: `http://localhost:8080`
4. Copy the following:
   - **Client ID** (under the app name)
   - **Client Secret**
5. Create a JSON file in `config/reddit_credentials.json`:

```json
{
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "user_agent": "ETL Script by u/YOUR_USERNAME"
}
```

---

## 2. ☁️ Google Cloud Setup (BigQuery)

### Step 1: Enable BigQuery API

- Visit: [https://console.cloud.google.com/apis/library](https://console.cloud.google.com/apis/library)
- Search for and enable: **BigQuery API**

### Step 2: Create a Service Account

1. Go to: [https://console.cloud.google.com/iam-admin/serviceaccounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
2. Click "Create Service Account"
3. Give it a name (e.g., `reddit-etl-service`)
4. Assign **BigQuery Data Editor** role
5. Save and **create a JSON key**
6. Place the JSON in `config/gcp_credentials.json`

---

### Step 3: Set Environment Variable (Windows)

Create a `.bat` file or set manually:

```bat
SET GOOGLE_APPLICATION_CREDENTIALS=C:\full\path\to\config\gcp_credentials.json
```

---

## 3. 🛠️ Create BigQuery Table

Manually or via script, create the dataset and table:

### Option A: Manually (Console)

1. Go to: [https://console.cloud.google.com/bigquery](https://console.cloud.google.com/bigquery)
2. Click on your project (e.g., `reddit-etl-236489`)
3. Click "Create Dataset": `reddit_etl`
4. Then click "Create Table":
   - Source: **Empty table**
   - Table name: `daily_posts`
   - Schema: Let it autodetect from first upload (or define manually)
   - Location: **US**
   - Click "Create"

---

### Option B: Programmatically (Python)

```python
from google.cloud import bigquery

client = bigquery.Client()

schema = [
    bigquery.SchemaField("id", "STRING"),
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("score", "INTEGER"),
    bigquery.SchemaField("num_comments", "INTEGER"),
    bigquery.SchemaField("author", "STRING"),
    bigquery.SchemaField("subreddit", "STRING"),
    bigquery.SchemaField("created_at", "TIMESTAMP"),
    bigquery.SchemaField("url", "STRING"),
    bigquery.SchemaField("selftext", "STRING"),
    bigquery.SchemaField("load_date", "TIMESTAMP"),
]

table_id = "reddit-etl-465703.reddit_etl.daily_posts"
table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)
print(f"Created table {table.table_id}")
```

---

## 4. 🐍 Python Dependencies

Install requirements with:

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```
praw
pandas
google-cloud-bigquery
pyarrow
```

---

## ✅ Ready to Go

Once everything is configured:

```bash
python main.py
```

New Reddit posts will load into BigQuery, and the Looker Studio dashboard will reflect updates!

---
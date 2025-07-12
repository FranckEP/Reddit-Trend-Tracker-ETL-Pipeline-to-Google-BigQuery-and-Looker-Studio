# Reddit Daily Trends ETL Pipeline

This project is an automated ETL pipeline that extracts trending posts from the **"technology"** subreddit using the Reddit API, transforms and loads the data into **Google BigQuery**, and visualizes it through **Looker Studio**.

---

## 🚀 Project Overview

- **Data Source**: Reddit API (`technology` subreddit)
- **ETL Stack**: Python (PRAW, pandas, BigQuery SDK)
- **Storage**: Google BigQuery
- **Visualization**: Looker Studio
- **Automation**: Windows Task Scheduler
- **Dashboard (public)**: [View on Looker Studio](https://lookerstudio.google.com/reporting/11114bb5-c170-4a6a-8f0d-9542a85e8578)

## 🧱 Components

### 1. `extract.py`
Uses `PRAW` to extract top 15 posts from the subreddit `technology`:
- Fields: `id`, `title`, `score`, `num_comments`, `author`, `created_utc`, etc.

### 2. `transform.py`
Processes raw data:
- Converts UNIX timestamps to datetime
- Truncates long text
- Adds `load_date` timestamp

### 3. `load.py`
Appends the cleaned DataFrame into a BigQuery table (`reddit_etl.daily_posts`) using:
- `bigquery.Client().load_table_from_dataframe()`

### 4. `main.py`
ETL Orchestration:
- Extracts → Transforms → Deduplicates (checks existing post IDs in BigQuery) → Loads new posts
- Prints results for logging and validation

---

## 🧪 Sample Output

```bash
        id        title         score   ...
0  xabc123   Apple launches ...   876   ...
1  xdef456   OpenAI partners ...   754   ...
```

---

## 📊 Looker Studio Dashboard

- Displays post volume, score trends, popular authors, and common keywords.
- Real-time updates from BigQuery.

🔗 [Dashboard Link](https://lookerstudio.google.com/reporting/11114bb5-c170-4a6a-8f0d-9542a85e8578)

---

## 🔁 Automation

### Windows Task Scheduler
1. Create `run_etl.bat` with:
```bat
@echo off
SET GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\gcp_credentials.json
cd C:\path\to\project
python main.py
```
2. Create a task to run this script daily at a fixed time.

---

## ✅ Results

- Data is pulled and updated **daily**
- Only **new, non-duplicate** posts are added
- Dashboard reflects latest Reddit discussions from r/technology

## 📌 Requirements

- Python 3.10+
- PRAW
- Google Cloud SDK (`google-cloud-bigquery`)
- pandas, pyarrow

Install dependencies:
```bash
pip install -r requirements.txt
```
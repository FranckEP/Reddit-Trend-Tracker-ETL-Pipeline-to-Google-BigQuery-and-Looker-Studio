# 📊 Reddit Daily Trends ETL Project

This project extracts top daily posts from the [r/technology](https://www.reddit.com/r/technology/) subreddit using the Reddit API and loads the cleaned data into **Google BigQuery**. The data is visualized using **Looker Studio** in a public dashboard.

🔗 **Dashboard**: [View on Looker Studio](https://lookerstudio.google.com/reporting/11114bb5-c170-4a6a-8f0d-9542a85e8578)

## 🔁 ETL Process Overview

1. **Extract**: Uses Reddit API (via `praw`) to pull daily top posts
2. **Transform**: Cleans and standardizes data, adds timestamps
3. **Load**: Uploads to BigQuery table `reddit_etl.daily_posts`
4. **Visualize**: Data is connected to a public Looker Studio dashboard

## 🛠️ Tech Stack

- Python
- PRAW (Reddit API wrapper)
- Google Cloud BigQuery
- Looker Studio (Data Visualization)
- Pandas


## 📁 Project Structure

```
Reddit-Trend-Tracker-ETL-Pipeline-to-Google-BigQuery-and-Looker-Studio/
├── config/
│   └── reddit_credentials.json
│   └── gcp_credentials.json
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── Reddit_ETL_Project_Documentation.md
├── Setup_and_Requirements_Guide
├── main.py
└── README.md
```

## 🚀 Quick Start

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/your-username/Reddit-Trend-Tracker-ETL.git
cd Reddit-Trend-Tracker-ETL
pip install -r requirements.txt
```

### 2. Setup API Keys

Follow the [Setup & Requirements Guide](./Setup_and_Requirements_Guide.md) to configure Reddit and GCP credentials.

### 3. Run the ETL Script

```bash
python main.py
```

## 📅 Automation

You can automate daily loads via **Windows Task Scheduler** or `cron` jobs (Linux/macOS). See the guide for instructions.

## 🧠 Insights

- Tracks daily trends from the tech subreddit
- Captures upvotes, comments, and authors
- Supports future features like sentiment analysis and keyword clustering

## 🧠 What I Learned

- Building production-ready ETL pipelines with API integrations
- Handling data deduplication with BigQuery
- Creating automated reporting with Google Looker Studio
- Setting up secure credentials and environment variables

## 📌 Author

**Franck Echeverría Peñaloza**  
# etl/extract.py
import praw
import json
import pandas as pd

def get_reddit_instance(config_path='config/reddit_credentials.json'):
    with open(config_path) as f:
        creds = json.load(f)
    reddit = praw.Reddit(client_id=creds['client_id'],
                         client_secret=creds['client_secret'],
                         user_agent=creds['user_agent'])
    return reddit

def extract_top_posts(subreddit_name='technology', limit=15):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.top(time_filter='day', limit=limit):
        posts.append({
            'id': post.id,
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'author': str(post.author),
            'subreddit': subreddit_name,
            'created_utc': post.created_utc,
            'url': post.url,
            'is_self': post.is_self,
            'selftext': post.selftext if post.is_self else ''
        })
    return pd.DataFrame(posts)

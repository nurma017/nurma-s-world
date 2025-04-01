import json
import csv
from datetime import datetime

def filter_news(news_list, keyword=None, date_from=None, date_to=None):
    filtered = []
    for news in news_list:
        if keyword and keyword.lower() not in news["title"].lower():
            continue
        filtered.append(news)
    return filtered

def save_news(news_list, filename="news", filetype="json"):
    if filetype == "json":
        with open(f"{filename}.json", "w") as f:
            json.dump(news_list, f, indent=4)
    elif filetype == "csv":
        with open(f"{filename}.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=news_list[0].keys())
            writer.writeheader()
            writer.writerows(news_list)
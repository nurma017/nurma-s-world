import json
import os

def save_data(user_id, data):
    with open(f"data_{user_id}.json", "w") as f:
        json.dump(data, f)

def load_data(user_id):
    if not os.path.exists(f"data_{user_id}.json"):
        return {}
    with open(f"data_{user_id}.json") as f:
        return json.load(f)
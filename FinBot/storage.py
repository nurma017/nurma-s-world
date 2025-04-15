import json
import os

def save_data(user_id, data):
    with open(f"data_{user_id}.json", "w") as f:
        json.dump(data, f)

def load_data(user_id):
    filename = f"data_{user_id}.json"
    if not os.path.exists(filename):
        return {}
    with open(filename) as f:
        return json.load(f)

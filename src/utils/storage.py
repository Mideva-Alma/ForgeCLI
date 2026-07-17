import json
import os

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data", "db.json",
)


def load_db(path=DB_PATH):
    if not os.path.exists(path):
        empty = {"users": [], "projects": [], "tasks": []}
        save_db(empty, path)
        return empty

    with open(path, "r") as f:
        content = f.read().strip()
        if not content:
            return {"users": [], "projects": [], "tasks": []}
        return json.loads(content)


def save_db(data, path=DB_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
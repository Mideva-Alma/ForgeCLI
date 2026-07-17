import os
from src.utils.storage import load_db, save_db


def test_load_creates_empty_db_if_missing(tmp_path):
    path = str(tmp_path / "db.json")
    assert not os.path.exists(path)
    db = load_db(path)
    assert db == {"users": [], "projects": [], "tasks": []}
    assert os.path.exists(path)


def test_save_and_load_round_trip(tmp_path):
    path = str(tmp_path / "db.json")
    data = {"users": [{"id": "1", "name": "Alex"}], "projects": [], "tasks": []}
    save_db(data, path)
    loaded = load_db(path)
    assert loaded == data
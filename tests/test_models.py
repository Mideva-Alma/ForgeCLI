from src.models import User, Project, Task


def test_create_user():
    u = User(name="Alex", email="alex@example.com")
    assert u.name == "Alex"
    assert u.email == "alex@example.com"
    assert u.project_ids == []


def test_empty_name_raises():
    try:
        User(name="   ")
        assert False, "Expected a ValueError"
    except ValueError:
        pass


def test_add_project_to_user():
    u = User(name="Alex")
    u.add_project("proj-1")
    assert u.project_ids == ["proj-1"]


def test_create_project():
    p = Project(name="CLI Tool", owner_id="u1", status="active")
    assert p.status == "active"
    assert p.task_ids == []


def test_task_mark_complete():
    t = Task(name="Write docs", project_id="p1")
    assert t.completed is False
    t.mark_complete()
    assert t.completed is True
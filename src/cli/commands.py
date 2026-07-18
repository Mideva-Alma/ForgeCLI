import sys
from rich.console import Console
from rich.table import Table
from src.models import User, Project, Task
from src.utils import load_db, save_db, find_by_name

console = Console()


def add_user(args):
    db = load_db()
    if find_by_name(db["users"], args.name):
        print(f"Error: user '{args.name}' already exists.")
        sys.exit(1)
    user = User(name=args.name, email=args.email)
    db["users"].append(user.to_dict())
    save_db(db)
    print(f"Created user {user.name} (id={user.id})")


def list_users(args):
    db = load_db()
    if not db["users"]:
        console.print("[yellow]No users yet.[/yellow]")
        return
    table = Table(title="Users")
    table.add_column("ID"); table.add_column("Name"); table.add_column("Email")
    for u in db["users"]:
        table.add_row(u["id"], u["name"], u.get("email") or "-")
    console.print(table)


def add_project(args):
    db = load_db()
    owner = find_by_name(db["users"], args.user)
    if owner is None:
        print(f"Error: user '{args.user}' not found.")
        sys.exit(1)
    project = Project(name=args.title, owner_id=owner["id"],
                       description=args.description or "",
                       status=args.status or "planned")
    db["projects"].append(project.to_dict())
    owner["project_ids"].append(project.id)
    save_db(db)
    print(f"Created project '{project.name}' (id={project.id}) for {owner['name']}")


def list_projects(args):
    db = load_db()
    projects = db["projects"]
    if getattr(args, "user", None):
        owner = find_by_name(db["users"], args.user)
        if owner is None:
            print(f"Error: user '{args.user}' not found.")
            sys.exit(1)
        projects = [p for p in projects if p["owner_id"] == owner["id"]]
    if not projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    table = Table(title="Projects")
    table.add_column("ID"); table.add_column("Title"); table.add_column("Status")
    for p in projects:
        table.add_row(p["id"], p["name"], p["status"])
    console.print(table)


def search_projects(args):
    db = load_db()
    query = args.query.strip().lower()
    matches = [p for p in db["projects"] if query in p["name"].lower()]
    if not matches:
        console.print(f"[yellow]No projects matching '{args.query}'.[/yellow]")
        return
    table = Table(title=f"Search: '{args.query}'")
    table.add_column("ID"); table.add_column("Title"); table.add_column("Status")
    for p in matches:
        table.add_row(p["id"], p["name"], p["status"])
    console.print(table)


def add_task(args):
    from dateutil import parser as date_parser

    db = load_db()
    project = find_by_name(db["projects"], args.project)
    if project is None:
        print(f"Error: project '{args.project}' not found.")
        sys.exit(1)

    due = None
    if args.due:
        due = date_parser.parse(args.due).date().isoformat()

    task = Task(name=args.title, project_id=project["id"],
                description=args.description or "", due_date=due)

    if args.contributor:
        for name in args.contributor:
            user = find_by_name(db["users"], name)
            if user:
                task.add_contributor(user["id"])

    db["tasks"].append(task.to_dict())
    project["task_ids"].append(task.id)
    save_db(db)
    print(f"Created task '{task.name}' (id={task.id}) under '{project['name']}'")


def list_tasks(args):
    db = load_db()
    if not db["tasks"]:
        console.print("[yellow]No tasks yet.[/yellow]")
        return
    table = Table(title="Tasks")
    table.add_column("ID"); table.add_column("Title"); table.add_column("Done")
    for t in db["tasks"]:
        table.add_row(t["id"], t["name"], "✔" if t["completed"] else "✘")
    console.print(table)


def complete_task(args):
    db = load_db()
    task = find_by_name(db["tasks"], args.title)
    if task is None:
        print(f"Error: task '{args.title}' not found.")
        sys.exit(1)
    task["completed"] = True
    save_db(db)
    print(f"Marked complete: {task['name']}")
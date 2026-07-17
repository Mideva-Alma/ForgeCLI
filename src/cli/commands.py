import sys
from src.models import User, Project, Task
from src.utils import load_db, save_db, find_by_name


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
        print("No users yet.")
        return
    for u in db["users"]:
        print(f"{u['id']}  {u['name']}  {u.get('email') or '-'}")


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
    if not db["projects"]:
        print("No projects yet.")
        return
    for p in db["projects"]:
        print(f"{p['id']}  {p['name']}  status={p['status']}")
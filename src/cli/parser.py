import argparse
from . import commands


def build_parser():
    parser = argparse.ArgumentParser(prog="pmtool", description="Project management CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("add-user", help="Create a new user")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=False)
    p.set_defaults(func=commands.add_user)

    p = sub.add_parser("list-users", help="List all users")
    p.set_defaults(func=commands.list_users)

    p = sub.add_parser("add-project", help="Create a project for a user")
    p.add_argument("--user", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--description", required=False, default="")
    p.add_argument("--status", required=False, choices=["planned", "active", "on-hold", "completed"])
    p.set_defaults(func=commands.add_project)

    p = sub.add_parser("list-projects", help="List projects, optionally filtered by user")
    p.add_argument("--user", required=False)
    p.set_defaults(func=commands.list_projects)

    p = sub.add_parser("search-projects", help="Search projects by title")
    p.add_argument("--query", required=True)
    p.set_defaults(func=commands.search_projects)

    p = sub.add_parser("add-task", help="Add a task to a project")
    p.add_argument("--project", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--description", required=False, default="")
    p.add_argument("--contributor", action="append")
    p.add_argument("--due", required=False, help="Due date e.g. '2026-08-01' or 'Aug 1'")
    p.set_defaults(func=commands.add_task)

    p = sub.add_parser("list-tasks", help="List all tasks")
    p.set_defaults(func=commands.list_tasks)

    p = sub.add_parser("complete-task", help="Mark a task as complete")
    p.add_argument("--title", required=True)
    p.set_defaults(func=commands.complete_task)

    return parser
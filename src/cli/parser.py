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

    p = sub.add_parser("list-projects", help="List all projects")
    p.set_defaults(func=commands.list_projects)

    return parser
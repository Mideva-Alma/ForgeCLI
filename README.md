# ForgeCLI — Project Management CLI Tool

A command-line tool for managing users, projects, and tasks, built with Python's `argparse`, JSON file persistence, and OOP design.

## Setup

\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Usage

\`\`\`bash
# Users
python3 main.py add-user --name "Alex" --email alex@example.com
python3 main.py list-users

# Projects
python3 main.py add-project --user "Alex" --title "CLI Tool" --status active
python3 main.py list-projects
python3 main.py list-projects --user "Alex"
python3 main.py search-projects --query cli

# Tasks
python3 main.py add-task --project "CLI Tool" --title "Write docs" --due "Aug 1 2026" --contributor Alex
python3 main.py list-tasks
python3 main.py complete-task --title "Write docs"
\`\`\`

## Running Tests

\`\`\`bash
python3 -m pytest tests/ -v
\`\`\`

## Project Structure

\`\`\`
ForgeCLI/
├── main.py              # entry point
├── requirements.txt
├── src/
│   ├── models/           # User, Project, Task classes
│   ├── cli/              # argparse parser + command logic
│   └── utils/            # JSON storage, lookup helpers
└── tests/                 # pytest test suite
\`\`\`

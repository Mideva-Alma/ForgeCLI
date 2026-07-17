from .base import Entity


class Task(Entity):
    def __init__(self, name, project_id, description="", completed=False,
                 due_date=None, contributor_ids=None, **kwargs):
        super().__init__(name, **kwargs)
        self.project_id = project_id
        self.description = description
        self.completed = completed
        self.due_date = due_date
        self.contributor_ids = contributor_ids or []

    def mark_complete(self):
        self.completed = True

    def add_contributor(self, user_id):
        if user_id not in self.contributor_ids:
            self.contributor_ids.append(user_id)

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "project_id": self.project_id,
            "description": self.description, "completed": self.completed,
            "due_date": self.due_date, "contributor_ids": self.contributor_ids,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"], project_id=data["project_id"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            due_date=data.get("due_date"),
            contributor_ids=data.get("contributor_ids", []),
            entity_id=data["id"], created_at=data.get("created_at"),
        )
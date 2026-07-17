from .base import Entity


class User(Entity):
    def __init__(self, name, email=None, project_ids=None, **kwargs):
        super().__init__(name, **kwargs)
        self.email = email
        self.project_ids = project_ids or []

    def add_project(self, project_id):
        if project_id not in self.project_ids:
            self.project_ids.append(project_id)

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "email": self.email,
            "project_ids": self.project_ids, "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"], email=data.get("email"),
            project_ids=data.get("project_ids", []),
            entity_id=data["id"], created_at=data.get("created_at"),
        )
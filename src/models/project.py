from .base import Entity

VALID_STATUSES = ("planned", "active", "on-hold", "completed")


class Project(Entity):
    def __init__(self, name, owner_id, description="", status="planned",
                 task_ids=None, **kwargs):
        super().__init__(name, **kwargs)
        self.owner_id = owner_id
        self.description = description
        if status not in VALID_STATUSES:
            raise ValueError(f"Status must be one of {VALID_STATUSES}")
        self.status = status
        self.task_ids = task_ids or []

    def add_task(self, task_id):
        if task_id not in self.task_ids:
            self.task_ids.append(task_id)

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "owner_id": self.owner_id,
            "description": self.description, "status": self.status,
            "task_ids": self.task_ids, "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"], owner_id=data["owner_id"],
            description=data.get("description", ""),
            status=data.get("status", "planned"),
            task_ids=data.get("task_ids", []),
            entity_id=data["id"], created_at=data.get("created_at"),
        )
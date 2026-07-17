import uuid
from abc import ABC, abstractmethod
from datetime import datetime


class Entity(ABC):
    def __init__(self, name, entity_id=None, created_at=None):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self.id = entity_id or str(uuid.uuid4())[:8]
        self.name = name.strip()
        self.created_at = created_at or datetime.now().isoformat(timespec="seconds")

    @abstractmethod
    def to_dict(self):
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass
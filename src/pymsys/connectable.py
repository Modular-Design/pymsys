from typing import Optional
from .interfaces import ISerializer
from .helpers import includes


class Connectable(ISerializer):
    def __init__(self,
                 id: Optional[object] = None,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 default_value: Optional[dict] = None,
                 removable: Optional[bool] = False):
        super().__init__()
        if id is None:
            import uuid
            id = str(uuid.uuid4())
        self.id = id
        self.name = name
        self.data = default_value
        self.description = description
        self.removable = removable

    def to_json(self) -> dict:
        res = dict()

        res["id"] = self.id
        res["removable"] = self.removable
        res["data"] = self.data

        if self.name:
            res["name"] = self.name

        if self.description:
            res["description"] = self.description
        return res

    def load(self, json: dict) -> bool:
        if "data" in json.keys():
            if not self.is_allowed(json["data"]):
                return False
            self.data = "data"
        return True

    def is_allowed(self, json: dict) -> bool:
        return includes(json.keys(), self.data.keys())


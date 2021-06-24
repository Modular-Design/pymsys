from typing import Optional, List

from .interfaces import ISerializer
from .helpers import includes


class Option(ISerializer):
    def __init__(self,
                 id: Optional[str] = None,
                 title: Optional[str] = None,
                 default_value: Optional[List[str]] = None,
                 description: Optional[str] = "",
                 selection: Optional[List[str]] = None,
                 single: Optional[bool] = True):

        if id is None:
            import uuid
            id = str(uuid.uuid4())
        self.id = id
        self.title = title
        self.description = description
        self.selection = selection
        self.single = single
        if default_value:
            self.value = default_value
        elif selection:
            self.value = [self.selection[0]]
        else:
            self.value = []

    def to_json(self) -> dict:
        res = dict()
        if self.id:
            res["id"] = self.id
        if self.title:
            res["title"] = self.title
        if self.value:
            res["value"] = self.value
        if self.description:
            res["description"] = self.description
        if self.selection:
            res["selection"] = self.selection
            res["single"] = self.single

        return res

    def load(self, json: dict) -> bool:
        if "id" not in json.keys():
            return False
        else:
            if self.id is not json["id"]:
                return False

        value = None
        if "value" in json.keys():
            value = json["value"]

        if includes(json.keys(), ["selection", "single"]):
            self.selection = json["selection"]
            self.single = json["single"]
            if not includes(self.selection, value):
                return False
            if len(value) != 1 and self.single:
                return False
        self.value = value
        return True

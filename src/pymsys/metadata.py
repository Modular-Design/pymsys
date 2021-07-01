from typing import Optional

from .interfaces import ISerializer


class Metadata(ISerializer):
    def __init__(self,
                 name: Optional[str] = None,
                 description: Optional[str] = None,):
        self.name = name
        self.description = description

    def to_dict(self) -> dict:
        res = dict()
        if self.name:
            res["name"] = self.name

        if self.description:
            res["description"] = self.description
        return res

    def load(self, json: dict) -> bool:
        return True
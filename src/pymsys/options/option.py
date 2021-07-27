from typing import Optional, List, Dict

from ..interfaces import ILink
from ..link import Link
from ..helpers import includes


class Option(Link):
    def __init__(self,
                 parent: Optional[ILink] = None,
                 title: Optional[str] = None,
                 default_value: Optional[List[str]] = None,
                 description: Optional[str] = "",
                 selection: Optional[List[str]] = None,
                 single: Optional[bool] = True,
                 influences: Optional[Dict[str, ILink]] = None):

        self.parent = parent
        self.title = title
        self.description = description
        self.selection = selection
        self.single = single
        self.value = []
        if default_value:
            self.value = default_value
        elif selection:
            self.value = [self.selection[0]]

        if influences is None:
            influences = []
        self.influences = influences

    def to_dict(self) -> dict:
        res = dict()
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

    def load(self, config: dict) -> bool:
        value = None
        if "value" in config.keys():
            value = config["value"]

        if includes(config.keys(), ["selection", "single"]):
            self.selection = config["selection"]
            self.single = config["single"]
            if not includes(self.selection, value):
                return False
            if len(value) != 1 and self.single:
                return False
        self.value = value
        return True


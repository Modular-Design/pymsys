from typing import Optional, List, Dict

from ..interfaces import ILink, IMetadata
from ..link import Link
from ..helpers import includes
from ..metadata import Metadata

class Option(Link):
    def __init__(self,
                 title: Optional[str] = None,
                 default_value: Optional[List[str]] = None,
                 description: Optional[str] = "",
                 selection: Optional[List[str]] = None,
                 single: Optional[bool] = True,
                 influences: Optional[Dict[str, ILink]] = None,
                 parent: Optional[ILink] = None,):

        self.meta = Metadata(name=title, description=description)
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

        super().__init__(childs={"meta": self.meta,
                                 "selection": self.selection,
                                 "value": self.value,
                                 "single": self.single})

    def get_meta(self) -> IMetadata:
        return self.meta

    def load(self, config: dict) -> bool:
        super().load(config)
        value = self.childs["value"]
        if self.selection:
            if not includes(self.selection, value):
                self.childs["value"] = self.value
                return False
            if len(value) != 1 and self.single:
                self.childs["value"] = self.vvalue
                return False
        return True


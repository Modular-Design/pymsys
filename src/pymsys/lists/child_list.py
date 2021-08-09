from ..link import Link, ILink
from typing import Optional, Dict
from ..interfaces import IGenerator


class ChildList(Link):
    def __init__(self,
                 childs: Optional[Dict[str, ILink]] = None,
                 key_generator: Optional[IGenerator] = None,
                 parent: Optional[ILink] = None,):
        super().__init__(parent=parent, childs=childs)
        self.generator = key_generator

        self.editable = bool(key_generator)

        if self.generator:
            self.generator.set_list(self)

    def set_editable(self, active: bool) -> bool:
        if not self.generator:
            return False
        self.editable = active
        return self.editable

    def to_dict(self) -> dict:
        res = {"size": len(self.childs),
               "editable": self.editable,
               "elements": super().to_dict()}
        if self.editable:
            res["execptions"] = self.generator.get_exceptions()
        return res

    def load(self, config: dict) -> bool:
        # determine diff
        diff = config["size"] - len(self.childs)
        if diff != 0 and not self.editable:
            raise ValueError
        else:
            if self.editable:
                self.generator.generate(diff, config["elements"])

        super().load(config["elements"])
        return True

    def __setitem__(self, elemno, elem):
        self.childs[elemno] = elem

    def __getitem__(self, elemno):
        return self.childs[elemno]

    def __len__(self):
        return len(self.childs)

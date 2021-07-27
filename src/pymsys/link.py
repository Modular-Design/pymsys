from typing import List, Optional, Dict
from .interfaces import ILink

class Link(ILink):
    def __init__(self,
                 parent: Optional[ILink] = None,
                 childs: Optional[Dict[str, ILink]] = None,
                 ):
        self.parent = parent

        if childs is None:
            childs = dict()
        self.childs = childs
        for key, child in self.childs.items():
            if isinstance(child, ILink):
                child.set_parent(self)

    def set_parent(self, parent: object) -> bool:
        self.parent = parent
        return True

    def find(self, keys: List[str]) -> object:
        if isinstance(keys, list):
            child = self.childs.get(keys[0])
            if len(keys) > 1 and isinstance(child, ILink):
                return child.find(keys[1:])
            return child
        else:
            return self.childs.get(str(keys))

    def get_childs(self) -> dict:
        return self.childs

    def get_key_from_child(self, child: ILink) -> str:
        try:
            index = list(self.childs.values()).index(child)
        except ValueError:
            return None
        return list(self.childs.keys())[index]

    def to_dict(self) -> dict:
        return dict((key, child.to_dict()) for key, child in self.childs.items())

    def load(self, config: dict) -> bool:
        for key, value in config.items():
            child = self.childs.get(key)
            if not child:
                continue
            child.load(value)
        return True

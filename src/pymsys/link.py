from typing import List, Optional, Dict, Union
from .interfaces import ILink


class Link(ILink):
    def __init__(self,
                 parent: Optional[Union[ILink]] = None,
                 childs: Optional[Dict[str, Union[ILink]]] = None,
                 ):

        self.parent = None
        self.set_parent(parent)

        if childs is None:
            childs = dict()
        self.childs = childs
        for key, child in self.childs.items():
            if isinstance(child, ILink):
                child.set_parent(self)

    def set_parent(self, parent: object) -> bool:
        self.parent = parent
        return True

    def get_parent(self) -> ILink:
        return self.parent

    def find(self, keys: List[str]) -> object:
        if isinstance(keys, list):
            child = self.childs.get(keys[0])
            if len(keys) > 1 and isinstance(child, ILink):
                return child.find(keys[1:])
            return child
        else:
            return self.childs.get(str(keys))

    def add_childs(self, childs: dict):
        for key, value in childs.items():
            value.set_parent(self.parent)

        self.childs.update(childs)

    def get_childs(self) -> dict:
        return self.childs

    def get_key_from_parent(self) -> str:
        if self.get_parent() is None:
            return None
        return self.get_parent().get_key_from_child(self)

    def get_key_from_child(self, child: ILink, depth: Optional[int] = 0) -> str:
        try:
            index = list(self.childs.values()).index(child)
        except ValueError:
            if depth > 0:
                for key, value in self.childs:
                    if not isinstance(value, ILink):
                        continue
                    keys = value.get_key_from_child(child, depth-1)
                    if keys is not None:
                        return [key] + list(keys)
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

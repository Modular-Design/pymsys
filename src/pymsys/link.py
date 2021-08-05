from typing import List, Optional, Dict, Union
from .interfaces import ILink, ISerializer


class Link(ILink):
    def __init__(self,
                 childs: Optional[Dict[str, Union[ILink, ISerializer]]] = None,
                 parent: Optional[Union[ILink]] = None,
                 ):

        self.parent = None
        self.flag = None
        self.set_parent(parent)

        if childs is None:
            childs = dict()
        self.childs = dict()
        self.add_childs(childs)

    def set_parent(self, parent: ILink, key: Optional[str] = None) -> bool:
        self.parent = parent
        if self.parent is not None:
            self.flag = key
        else:
            self.flag = None
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
        for key, child in childs.items():
            if isinstance(child, ILink):
                child.set_parent(self, key)
        self.childs.update(childs)

    def get_childs(self) -> dict:
        return self.childs

    def get_key_from_parent(self) -> Union[str, None]:
        return self.flag

    def get_key_from_child(self, child: ILink, depth: Optional[int] = 0) -> Union[List[str], None]:
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
        print("get_key_from_child" + str(index))
        return list(self.childs.keys())[index]

    def to_dict(self) -> dict:
        res = dict()
        for key, child in self.childs.items():
            if isinstance(child, ISerializer):
                res[key] = child.to_dict()
            else:
                res[key] = child
        return res

    def load(self, config: dict) -> bool:
        for key, value in config.items():
            child = self.childs.get(key)
            if isinstance(child, ISerializer):
                child.load(value)
            else:
                self.childs[key] = value

        return True

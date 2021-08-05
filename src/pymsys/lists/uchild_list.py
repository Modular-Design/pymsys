from ..link import ILink
from typing import Optional, Dict, List, Union
from ..interfaces import IGenerator, IUpdatable
from .child_list import ChildList


class UpdatableChildList(ChildList, IUpdatable):
    def __init__(self,
                 childs: Optional[Dict[str, Union[ILink, IUpdatable]]] = None,
                 key_generator: Optional[IGenerator] = None,
                 parent: Optional[ILink] = None,
                 ):
        super().__init__(childs=childs, key_generator=key_generator, parent=parent)

    def update(self) -> List[int]:
        res = []
        for key, child in self.childs.items():
            temp = child.update()
            while len(temp) - len(res) > 0:
                res.append(0)
            for i in range(len(temp)):
                res[i] = res[i] + temp[i]
        return res

    def is_changed(self) -> List[int]:
        res = []
        for key, child in self.childs.items():
            temp = child.is_changed()
            while len(temp) - len(res) > 0:
                res.append(0)
            for i in range(len(temp)):
                res[i] = res[i] + temp[i]
        return res
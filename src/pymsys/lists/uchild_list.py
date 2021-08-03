from ..link import Link, ILink
from typing import Optional, Dict, List, Union
from ..interfaces import IGenerator, IUpdatable


class UpdatableChildList(Link, IUpdatable):
    def __init__(self,
                 parent: Optional[ILink] = None,
                 childs: Optional[Dict[str, Union[ILink, IUpdatable]]] = None,
                 key_generator: Optional[IGenerator] = None,):
        super().__init__(parent, childs, key_generator)

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
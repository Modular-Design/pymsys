from ..interfaces import IGenerator, ILink
from typing import Optional, List


class Generator(IGenerator):
    def __init__(self,
                 class_obj,
                 parent: Optional[ILink] = None,
                 min_child_limit: Optional[int] = 0,
                 initial_size: Optional[int] = 0
                 ):

        self.class_obj = class_obj
        # sanity check
        if not isinstance(self.class_obj(), ILink):
            raise TypeError

        self.parent = parent

        self.exceptions = []

        self.min_limit = min_child_limit
        self.initial_size = initial_size
        pass

    def set_list(self, child_list: ILink) -> bool:
        self.parent = child_list
        if self.parent is None:
            return True

        keys = list(self.parent.get_childs().keys())

        if not self.exceptions:
            self.exceptions = keys
            self.min_limit = len(keys)

        if self.initial_size > len(keys):
            self.generate(self.initial_size-len(keys))

        return True

    def get_exceptions(self) -> List[str]:
        return self.exceptions

    def generate(self, diff: int, new_key_list: Optional[List[str]] = None):
        keys = list(self.parent.get_childs().keys())
        if diff > 0:
            for i in range(diff):
                child = self.class_obj()
                self.parent.get_childs().update({self.generate_key(): child})
            pass
        if diff < 0:
            if new_key_list is None:
                new_key_list = []
            if diff == len(new_key_list) - len(self.parent.childs.keys()):
                findings = 0
                for key in keys:
                    if key not in new_key_list:
                        self.parent.get_childs().pop(key)
                        findings = findings - 1
                        if diff == findings:
                            break
            else:
                for i in range(abs(diff)):
                    keys = list(self.parent.get_childs().keys())
                    if len(keys) <= self.min_limit:
                        break

                    for i in range(len(keys)):
                        key = keys[-(i+1)]
                        if key not in self.exceptions:
                            self.parent.get_childs().pop(key)
                            break
            pass

    def generate_key(self) -> str:
        raise NotImplementedError

    def key_fits(self) -> bool:
        return True

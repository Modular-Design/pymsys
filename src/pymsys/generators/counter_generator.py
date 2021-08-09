from .generator import Generator
from typing import Optional


class CounterGenerator(Generator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_key(self, key: Optional[str] = None) -> str:
        number = len(self.parent.get_childs())
        for i in range(number):
            key = str(i)
            if not self.parent.get_childs().get(key):
                return key
        return str(number)

    def sort(self):
        childs = self.parent.get_childs()
        res = dict()
        for i in sorted(childs):
            res[i] = childs[i]
        self.parent.childs = res
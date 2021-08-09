from ..interfaces import IValue, IConnectable
from ..helpers import includes
from typing import Optional, List, Union, Any
from ..helpers import encrypt
from ..link import Link


class Value(Link, IValue):
    def __init__(self,
                 default_data: Optional[Union[dict, float, int, str]] = None,
                 parent: Optional["IConnectable"] = None,):
        if default_data is None:
            default_data = dict()
        elif isinstance(default_data, float) or isinstance(default_data, int):
            default_data = dict(value=default_data)
        elif isinstance(default_data, str):
            default_data = dict(text=default_data)
        self.connectable = None
        self.last_hash = encrypt(default_data)
        self.default_data = default_data
        super().__init__(default_data, parent)

    def load(self, config: dict) -> bool:
        if not self.is_allowed(config):
            return False
        super().load(config)
        return True

    def set_data(self, data)-> bool:
        if self.is_allowed(data):
            self.default_data = data
            self.childs = data
            return True
        return False

    def get_data(self) -> Any:
        return self.childs

    def is_allowed(self, config: dict) -> bool:
        return includes(config.keys(), self.default_data.keys())

    def update(self) -> List[int]:
        hash = encrypt(self.childs)
        res = self.is_changed()
        self.last_hash = hash
        return res

    def is_changed(self) -> List[int]:
        return [int(encrypt(self.childs) == self.last_hash)]

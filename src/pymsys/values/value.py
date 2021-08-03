from ..interfaces import IValue
from ..helpers import includes
from typing import Optional, List
from ..helpers import encrypt


class Value(IValue):
    def __init__(self, default_value: Optional[dict] = None):
        if default_value is None:
            default_value = dict()
        self.connectable = None
        self.value = default_value
        self.last_hash = encrypt(self.value)

    def to_dict(self) -> dict:
        return self.value

    def load(self, config: dict) -> bool:
        if not self.is_allowed(config):
            raise ValueError("Value is not allowed!")
        self.value = config
        return True

    def set_connectable(self, connectable: "Connectable") -> bool:
        self.connectable = connectable
        return True

    def is_allowed(self, config: dict) -> bool:
        return includes(config.keys(), self.value.keys())

    def update(self) -> List[int]:
        hash = encrypt(self.value)
        res = self.is_changed()
        self.last_hash = hash
        return [int(res)]

    def is_changed(self) -> List[int]:
        return [int(encrypt(self.get_data()) == self.last_hash)]

from ..interfaces import IValue
from ..helpers import includes
from typing import  Optional

class Value(IValue):
    def __init__(self, default_value: Optional[dict] = None):
        if default_value is None:
            default_value = dict()
        self.value = default_value

    def to_dict(self) -> dict:
        return self.value

    def load(self, config: dict) -> bool:
        if not self.is_allowed(config):
            return False
        self.value = config
        return True

    def is_allowed(self, config: dict) -> bool:
        return includes(config.keys(), self.value.keys())

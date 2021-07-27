from abc import ABC, abstractmethod
from .iserializer import ISerializer


class IValue(ISerializer):
    @abstractmethod
    def is_allowed(self, config: dict) -> bool:
        pass
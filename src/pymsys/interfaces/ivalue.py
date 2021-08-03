from abc import abstractmethod
from .iserializer import ISerializer
from .iupdatable import IUpdatable


class IValue(ISerializer, IUpdatable):
    @abstractmethod
    def set_connectable(self, connectable: "Connectable") -> bool:
        pass

    @abstractmethod
    def is_allowed(self, config: dict) -> bool:
        pass
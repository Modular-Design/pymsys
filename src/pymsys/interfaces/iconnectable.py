from abc import abstractmethod
from typing import List
from .ilink import ILink
from .isetable import ISetable
from .imeta import IMeta


class IConnectable(ILink, ISetable, IMeta):
    @abstractmethod
    def get_output(self) -> "IConnectable":
        pass

    @abstractmethod
    def set_ingoing(self, connection: "IConnection"):
        pass

    @abstractmethod
    def get_inputs(self) -> List["IConnectable"]:
        pass

    @abstractmethod
    def set_outgoing(self, connections: List["Connection"]) -> None:
        pass

    @abstractmethod
    def add_outgoing(self, connection: "Connection") -> None:
        pass

    @abstractmethod
    def remove_outgoing(self, connection: "Connection") -> None:
        pass

    @abstractmethod
    def is_allowed(self, config: dict) -> bool:
        pass

    @abstractmethod
    def is_connectable(self, output: "IConnectable"):
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

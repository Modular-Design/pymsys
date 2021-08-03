from abc import abstractmethod
from typing import List
from .iserializer import ISerializer
from .ilink import ILink


class IConnectable(ISerializer, ILink):
    @abstractmethod
    def get_data(self) -> dict:
        pass

    @abstractmethod
    def set_data(self, data) -> bool:
        pass

    @abstractmethod
    def get_output(self) -> "IConnectable":
        pass

    @abstractmethod
    def set_ingoing(self, connection: "Connection"):
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
    def is_data_valid(self, data: dict):
        pass

    @abstractmethod
    def is_connectable(self, output: "IConnectable"):
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

from abc import abstractmethod
from .ilink import ILink
from .iconnectable import IConnectable


class IConnection(ILink):
    @abstractmethod
    def get_input(self) -> "IConnectable":
        pass

    @abstractmethod
    def get_output(self) -> "IConnectable":
        pass

    @abstractmethod
    def connect(self, output: "IConnectable", input: "IConnectable") -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

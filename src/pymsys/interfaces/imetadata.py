from abc import ABC, abstractmethod
from .iserializer import ISerializer


class IMetadata(ISerializer):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def set_description(self, description: str) -> None:
        pass

    @abstractmethod
    def get_info(self) -> dict:
        pass
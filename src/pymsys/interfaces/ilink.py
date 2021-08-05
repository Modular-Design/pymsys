from abc import ABC, abstractmethod
from typing import List, Optional, Union
from .iserializer import ISerializer


class ILink(ISerializer):
    @abstractmethod
    def set_parent(self, parent: "ILink", key: Optional[str] = None) -> bool:
        pass

    @abstractmethod
    def get_parent(self) -> "ILink":
        pass

    @abstractmethod
    def find(self, keys: List[str]) -> object:
        pass

    @abstractmethod
    def add_childs(self, childs: dict):
        pass

    @abstractmethod
    def get_childs(self) -> dict:
        pass

    @abstractmethod
    def get_key_from_parent(self) -> Union[str, None]:
        pass

    @abstractmethod
    def get_key_from_child(self, child: "ILink", depth: Optional[int] = 0) -> Union[List[str], None]:
        pass

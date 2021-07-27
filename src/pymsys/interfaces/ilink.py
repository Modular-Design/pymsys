from abc import ABC, abstractmethod
from typing import List
from .iserializer import ISerializer


class ILink(ISerializer):
    @abstractmethod
    def set_parent(self, parent: "ILink") -> bool:
        pass

    @abstractmethod
    def find(self, keys: List[str]) -> object:
        pass

    @abstractmethod
    def get_childs(self) -> dict:
        pass

    @abstractmethod
    def get_key_from_child(self, child: "ILink") -> str:
        pass

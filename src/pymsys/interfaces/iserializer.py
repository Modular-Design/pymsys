from abc import ABC, abstractmethod


class ISerializer(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass

    @abstractmethod
    def load(self, json: dict) -> bool:
        pass


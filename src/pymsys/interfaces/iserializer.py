from abc import ABC, abstractmethod


class ISerializer(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def load(self, config: dict) -> bool:
        pass


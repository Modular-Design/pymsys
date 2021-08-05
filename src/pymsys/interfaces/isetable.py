from abc import ABC, abstractmethod
from typing import Any


class ISetable(ABC):
    @abstractmethod
    def set_data(self, data) -> bool:
        pass

    @abstractmethod
    def get_data(self) -> Any:
        pass

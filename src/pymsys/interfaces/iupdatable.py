from abc import ABC, abstractmethod
from typing import List


class IUpdatable(ABC):
    @abstractmethod
    def update(self) -> List[int]:
        pass

    @abstractmethod
    def is_changed(self) -> List[int]:
        pass

from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .ilink import ILink


class IGenerator(ABC):
    @abstractmethod
    def set_list(self, child_list: ILink) -> bool:
        pass

    @abstractmethod
    def get_exceptions(self) -> List[str]:
        pass

    @abstractmethod
    def generate(self, diff: int, new_config: Dict[str, Any]):
        pass

    @abstractmethod
    def key_fits(self) -> bool:
        pass

from abc import ABC, abstractmethod
from .imetadata import IMetadata


class IMeta(ABC):
    @abstractmethod
    def get_meta(self) -> IMetadata:
        pass


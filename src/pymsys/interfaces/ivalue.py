from abc import abstractmethod
from .ilink import ILink
from .iupdatable import IUpdatable
from .iconnectable import IConnectable
from .isetable import ISetable


class IValue(ILink, IUpdatable, ISetable):

    @abstractmethod
    def is_allowed(self, config: dict) -> bool:
        pass

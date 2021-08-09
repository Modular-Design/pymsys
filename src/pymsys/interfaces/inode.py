from .ilink import ILink
from .iupdatable import IUpdatable
from .iconnectable import IConnectable
from .imeta import IMeta
from .ioption import IOption

from typing import List
from abc import abstractmethod


class INode(ILink, IUpdatable, IMeta):
    @abstractmethod
    def get_inputs(self) -> List[IConnectable]:
        pass

    @abstractmethod
    def get_outputs(self) -> List[IConnectable]:
        pass

    @abstractmethod
    def get_options(self) -> List["IOption"]:
        pass

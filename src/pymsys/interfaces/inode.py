from .ilink import ILink
from .iupdatable import IUpdatable
from .iconnectable import IConnectable

from typing import List
from abc import abstractmethod


class INode(ILink, IUpdatable):
    @abstractmethod
    def get_inputs(self, local=False) -> List[IConnectable]:
        raise NotImplementedError

    @abstractmethod
    def get_outputs(self, local=False) -> List[IConnectable]:
        raise NotImplementedError

    @abstractmethod
    def get_options(self) -> List["Option"]:
        pass

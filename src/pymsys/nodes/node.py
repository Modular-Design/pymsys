from abc import ABC, abstractmethod
from typing import Optional, Dict

from ..connectables import Connectable
from ..metadata import Metadata
from ..options import Option
from ..interfaces import IGenerator, ILink, IMetadata
from ..link import Link
from ..child_list import ChildList


class Node(Link, ABC):
    def __init__(self,
                 parent: Optional[ILink] = None,
                 meta: Optional[IMetadata] = None,
                 inputs: Optional[Dict[str, Connectable]] = None,
                 outputs: Optional[Dict[str, Connectable]] = None,
                 options: Optional[Dict[str, Option]] = None,
                 input_generator: Optional[IGenerator] = False,
                 output_generator: Optional[IGenerator] = False,
                 option_generator: Optional[IGenerator] = None,
                 ram_reserve: Optional[float] = 0.0,):

        if meta is None:
            meta = Metadata()
        self.meta = meta

        self.inputs = ChildList(self, inputs, input_generator)
        self.outputs = ChildList(self, outputs, output_generator)
        self.options = ChildList(self, options, option_generator)

        super().__init__(parent, {
                                "meta": self.meta,
                                "options": self.options,
                                "inputs": self.inputs,
                                "outputs": self.outputs,
                                }
                         )
        self.ram_reserve = ram_reserve  # mb

    def to_dict(self) -> dict:
        res = super().to_dict()
        res["ram"] = self.ram_reserve
        return res

    @abstractmethod
    def update(self):
        pass

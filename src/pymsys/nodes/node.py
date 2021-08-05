from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Type

from ..metadata import Metadata
from ..options import Option
from ..interfaces import IGenerator, ILink, IMetadata, INode, IConnectable
from ..link import Link
from ..lists import ChildList, UpdatableChildList


class Node(Link, INode, ABC):
    def __init__(self,
                 meta: Optional[IMetadata] = None,
                 inputs: Optional[Dict[str, IConnectable]] = None,
                 outputs: Optional[Dict[str, IConnectable]] = None,
                 options: Optional[Dict[str, Option]] = None,
                 input_generator: Optional[IGenerator] = None,
                 output_generator: Optional[IGenerator] = None,
                 option_generator: Optional[IGenerator] = None,
                 input_list: Optional[Type[ChildList]] = UpdatableChildList,
                 output_list: Optional[Type[ChildList]] = UpdatableChildList,
                 option_list: Optional[Type[ChildList]] = ChildList,
                 ram_reserve: Optional[float] = 0.0,
                 parent: Optional[ILink] = None,
                 **kwargs,
                 ):

        if meta is None:
            meta = Metadata()
        self.meta = meta

        self.inputs = input_list(inputs, input_generator)
        self.outputs = output_list(outputs, output_generator)
        self.options = option_list(options, option_generator)
        self.ram_reserve = ram_reserve
        childs = kwargs
        childs.update({
            "meta": self.meta,
            "options": self.options,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "ram": self.ram_reserve,
            })

        super().__init__(parent=parent, childs=childs)
          # mb
        self.change = []

    def to_dict(self) -> dict:
        res = super().to_dict()
        return res

    def get_meta(self) -> IMetadata:
        return self.meta

    def get_inputs(self) -> List[IConnectable]:
        return self.inputs[:]

    def get_outputs(self) -> List[IConnectable]:
        return self.outputs[:]

    def get_options(self) -> List["Option"]:
        return self.options[:]

    def update(self):
        input_change = self.inputs.update()

        self.process(bool(input_change[0]))

        output_change = self.outputs.update()

        self.change = input_change + output_change
        return self.change

    def is_changed(self) -> List[int]:
        return self.change

    @abstractmethod
    def process(self, input_changed: bool):
        pass

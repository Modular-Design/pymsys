from abc import ABC, abstractmethod
from typing import Optional, List

from .connectable import Connectable
from .metadata import Metadata
from .option import Option
from .interfaces import ISerializer


class Module(ISerializer, ABC):
    def __init__(self,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 inputs: Optional[List[Connectable]] = None,
                 outputs: Optional[List[Connectable]] = None,
                 options: Optional[List[Option]] = None,
                 removable_inputs: Optional[bool] = False,
                 removable_outputs: Optional[bool] = False,
                 ram_reserve: Optional[float] = 0.0,):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.options = options
        self.removable_inputs = removable_inputs
        self.removable_outputs = removable_outputs
        self.meta = Metadata(name, description)
        self.ram_reserve = ram_reserve  # mb

    def to_dict(self) -> dict:
        res = dict()
        res["ram"] = self.ram_reserve
        res["meta"] = self.meta.to_dict()

        if self.options:
            res["options"] = {"size": len(self.options), "addable": False, "elements": []}
            for opt in self.options:
                res["options"]["elements"].append(opt.to_dict())

        if self.inputs:
            res["inputs"] = {"size": len(self.inputs), "removable": self.removable_inputs, "elements": []}
            for inp in self.inputs:
                res["inputs"]["elements"].append(inp.to_dict())

        if self.outputs:
            res["outputs"] = {"size": len(self.outputs), "removable": self.removable_outputs, "elements": []}
            for out in self.outputs:
                res["outputs"]["elements"].append(out.to_dict())

        return res

    def load(self, json: dict) -> bool:
        if "options" in json.keys():
            options = json["options"]
            if options["size"] != len(self.options):
                return False
            for opt in options["elements"]:
                for option in self.options:
                    if option.id == opt["id"]:
                        if not option.load(opt):
                            return False
                        break

        if "inputs" in json.keys():
            inputs = json["inputs"]
            diff = inputs["size"] - self.inputs
            if diff != 0 and not self.removable_inputs:
                return False
            if diff > 0:
                self.generate_inputs(diff)

            if diff < 0:
                self.erase_inputs(diff)

            for inp in inputs["elements"]:
                for input in self.inputs:
                    if input.id == inp["id"]:
                        if not input.load(inp):
                            return False
                        found = True
                        break

        if "outputs" in json.keys():
            outputs = json["outputs"]
            diff = outputs["size"] - self.outputs
            if diff != 0 and not self.removable_outputs:
                return False
            if diff > 0:
                self.generate_outputs(diff)

            if diff < 0:
                self.erase_outputs(diff)

            for out in outputs["elements"]:
                for output in self.outputs:
                    if output.id == out["id"]:
                        if not output.load(out):
                            return False
                        break

        return True

    def generate_inputs(self, diff: int) -> bool:
        if not self.removable_inputs:
            return False
        return True

    def erase_inputs(self, diff: int) -> bool:
        if not self.removable_inputs:
            return False
        return True

    def generate_outputs(self, diff: int) -> bool:
        if not self.removable_outputs:
            return False
        return True

    def erase_outputs(self, diff: int) -> bool:
        if not self.removable_outputs:
            return False
        return True

    @abstractmethod
    def update(self):
        pass

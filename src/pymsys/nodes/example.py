from .node import *
from ..connectables import Connectable
from ..generators import CounterGenerator
from ..server import Server


class ExampleNode(Node):
    def __init__(self):
        super().__init__(meta=Metadata(name="ExampleModule",
                                       description="This is a example Module",),
                         options={"insert": Option(
                                         title="Insert",
                                         description="Insert something!",
                                         default_value=["something"],
                                         ),
                                  "choose_one": Option(
                                         title="Choose One",
                                         description="Choose one of the folowing!",
                                         selection=["1", "2", "3"],
                                         ),
                                  "choose_multiple": Option(
                                         title="Choose Multiple",
                                         description="Choose one or more of the folowing!",
                                         selection=["1", "2", "3"],
                                         single=False)},
                         inputs={"blocked": Connectable(
                             meta=Metadata(name="blocked",
                                           description="Insert something!",),
                             data=1,
                         )},
                         input_generator=CounterGenerator(default_class=Connectable, initial_size=4, default_config={"data":{"value": 1}}),
                         output_generator=CounterGenerator(default_class=Connectable, initial_size=3, default_config={"data":{"value": 1}}))

    def process(self, input_changed: bool) -> bool:
        print(self.inputs.childs.keys())
        print(self.outputs.childs.keys())
        for i in range(3):
            self.outputs[str(i)].load(self.inputs[str(i)].to_dict())
        return True


example = Server(ExampleNode)

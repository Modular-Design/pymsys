from .node import *
from ..connectables import Connectable
from ..generators import CounterGenerator
from ..server import Server


class ExampleNode(Node):
    def __init__(self):
        super().__init__(meta= Metadata(name="ExampleModule", description="This is a example Module",),
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
                             meta= Metadata(name="blocked",description="Insert something!",),
                             data={"value": 1},
                         )},
                         input_generator=CounterGenerator(class_obj=Connectable, initial_size=4),
                         output_generator=CounterGenerator(class_obj=Connectable, initial_size=3))

    def update(self) -> bool:
        for i in range(3):
            self.outputs[str(i)].load(self.inputs[str(i)].to_dict())
        return True


example = Server(ExampleNode)

from .module import *
from .option import *
from .connectable import Connectable


class ExampleModule(Module):
    def __init__(self):
        super().__init__(name="ExampleModule",
                         description="This is a example Module",
                         inputs=[Connectable(id="0",
                                             name="in0",
                                             description="first input",
                                             ),
                                 Connectable(id="1",
                                             name="in1",
                                             description="second input"),
                                 Connectable(id="2",
                                             name="in2",
                                             description="third input"),
                                 ],
                         outputs=[Connectable(id="0",
                                              name="out0",
                                              description="first output"),
                                  Connectable(id="1",
                                              name="out1",
                                              description="second output"),
                                  Connectable(id="2",
                                              name="out2",
                                              description="third output"),
                                  ],
                         options=[Option(id="insert",
                                         title="Insert",
                                         description="Insert something!",
                                         default_value="something",
                                         ),
                                  Option(id="choose_one",
                                         title="Choose One",
                                         description="Choose one of the folowing!",
                                         selection=["1", "2", "3"],
                                         ),
                                  Option(id="choose_multiple",
                                         title="Choose Multiple",
                                         description="Choose one or more of the folowing!",
                                         selection=["1", "2", "3"],
                                         single=False)],
                         removable_inputs=True,
                         removable_outputs=True)

    def update(self) -> bool:
        for i in range(3):
            self.outputs[i].load(self.inputs[i].to_dict())
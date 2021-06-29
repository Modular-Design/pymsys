from ..module import *
from ..option import *
from ..connectable import Connectable
from ..server import Server


class TestModule(Module):
    def __init__(self):
        super().__init__(name="Test",
                         description="This is a Testmodule",
                         inputs=[Connectable(), Connectable(), Connectable()],
                         outputs=[Connectable(), Connectable(), Connectable()],
                         options=[Option(), Option(), Option()],
                         removable_inputs=True,
                         removable_outputs=True)

    def update(self) -> bool:
        pass


app = Server(TestModule)

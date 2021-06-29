from src.pymsys.module import *
from src.pymsys.option import *
from src.pymsys.connectable import Connectable


class TestModule(Module):
    def __init__(self):
        super().__init__(name="Test",
                         description="This is a Testmodule",
                         inputs=[Connectable(), Connectable(), Connectable()],
                         outputs=[Connectable(), Connectable(), Connectable()],
                         options=[Option(), Option(), Option()],
                         removable_inputs=True,
                         removable_outputs=True)

    def process(self) -> bool:
        pass


app = TestModule()
if __name__ == "__main__":
    import uvicorn
    obj = uvicorn.run("test:app",)
    print(obj.__dict__)

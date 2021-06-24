from src.pymsys.module import *
from src.pymsys.option import *
from src.pymsys.connectable import Connectable


class TestModule(Module):
    def __init__(self):
        super().__init__(url="http://127.0.0.1:9000/docs#/registration/lists_registration_get",
                         name="Test",
                         description="This is a Testmodule",
                         inputs=[Connectable(), Connectable(), Connectable()],
                         outputs=[Connectable(), Connectable(), Connectable()],
                         options=[Option(), Option(), Option()],
                         addable_inputs=True,
                         addable_outputs=True)

    def process(self) -> bool:
        pass


app = TestModule()
if __name__ == "__main__":
    import uvicorn
    obj = uvicorn.run("test:app",)
    print(obj.__dict__)

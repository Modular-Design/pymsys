from .generator import Generator
import uuid


class UUIDGenerator(Generator):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def generate_key(self) -> str:
        return str(uuid.uuid4())

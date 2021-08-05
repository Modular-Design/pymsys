from .generator import Generator
import uuid
from typing import Optional


class UUIDGenerator(Generator):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def generate_key(self, key: Optional[str] = None) -> str:
        return str(uuid.uuid4())

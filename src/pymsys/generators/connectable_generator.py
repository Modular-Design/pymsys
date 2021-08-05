from .uuid_generator import UUIDGenerator
from ..interfaces import ILink, IValue
from ..connectables import Connectable
from ..values import Value
from typing import Optional, Type


class ConnectableGenerator(UUIDGenerator):
    def __init__(
            self,
            default_value_class: Optional[Type[IValue]] = Value,
            **kwargs,
    ):
        super().__init__(**kwargs)
        self.default_value_class = default_value_class

    def generate_class(self, key: Optional[str] = None) -> ILink:
        return Connectable(default_value_class=self.default_value_class)

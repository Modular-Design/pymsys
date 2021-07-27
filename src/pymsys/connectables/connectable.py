from typing import Optional
from ..link import Link, ILink

from ..metadata import Metadata
from ..values import Value
from ..interfaces import IValue, IMetadata



class Connectable(Link):
    def __init__(self,
                 parent: Optional[ILink] = None,
                 meta: Optional[IMetadata] = None,
                 data: Optional[IValue] = None,):

        self.parent = parent
        if meta is None:
            meta = Metadata()
        self.meta = meta
        if data is None:
            data = Value()
        if not isinstance(data, IValue):
            data = Value(data)
        self.data = data

        super().__init__(parent, {"meta": self.meta,
                                  "data": self.data})




import weakref
from typing import Optional, List, Union, Type
from ..link import Link, ILink

from ..metadata import Metadata
from ..values import Value
from ..interfaces import IValue, IMetadata, IConnectable, IConnection

CONNECTABLE_FLAGS = {"inputs", "outputs"}


class Connectable(Link, IConnectable):
    def __init__(self,
                 meta: Optional[IMetadata] = None,
                 data: Optional[Union[IValue, dict, float, str]] = None,
                 parent: Optional[ILink] = None,
                 default_value_class: Optional[Type[IValue]] = Value,
                 ):

        self.parent = parent
        if meta is None:
            meta = Metadata()
        self.meta = meta
        if data is None:
            data = default_value_class()
        if not isinstance(data, IValue):
            data = default_value_class(data)
        self.data = data

        self.in_ref = None
        self.out_refs = []

        super().__init__(childs={"meta": self.meta,
                                 "data": self.data},
                         parent=parent)

    def get_data(self):
        return self.data

    def set_data(self, data) -> bool:
        return self.data.set_data(data)

    def get_local(self) -> str:
        if self.flag is None:
            return self.flag
        if self.flag not in CONNECTABLE_FLAGS:
            raise KeyError
        return list(CONNECTABLE_FLAGS - set(self.flag))[0]

    def get_global(self) -> str:
        return self.flag

    def get_output(self) -> IConnectable:
        if not self.in_ref:
            return None
        connection = self.in_ref()
        if not connection:
            return None
        return connection.get_output()

    def get_inputs(self) -> List[IConnectable]:
        res = []
        for i in range(len(self.out_refs)):
            connection = self.out_refs[i]()
            if not connection:
                del self.out_refs[i]
            input = connection.get_input()
            if input:
                res.append(input)
        return res

    def get_meta(self) -> IMetadata:
        return self.meta

    def get_data(self):
        output = self.get_output()
        if output:
            output.get_data()

        return self.data

    def update(self) -> List[int]:
        return self.data.update()

    def is_changed(self) -> List[int]:
        return self.data.is_changed()

    def is_connectable(self, output: IConnectable) -> bool:
        return self.get_data().is_allowed(output.get_data())

    def set_ingoing(self, connection: "IConnection"):
        if self.in_ref:
            conn = self.in_ref()
            if conn is not connection:
                conn.disconnect()
        self.in_ref = weakref.ref(connection)

    def set_outgoing(self, connections: List["IConnection"]):
        for i in range(len(self.out_refs)):
            conn = self.out_refs[i]()
            if conn not in connections:
                conn.disconnect()

        self.out_refs = []
        for conn in connections:
            self.add_outgoing(conn)

    def add_outgoing(self, connection: "IConnection"):
        found = False
        for i in range(len(self.out_refs)):
            conn_ref = self.out_refs[i]
            if conn_ref() is connection:
                found = True
                break

        if not found:
            self.outgoing.append(weakref.ref(connection))

    def remove_outgoing(self, connection: "IConnection"):
        for i in range(len(self.out_refs)):
            conn_ref = self.out_refs[i]
            if conn_ref() is connection:
                del self.out_refs[i]

    def is_allowed(self, config: dict) -> bool:
        return self.data.is_allowed(config)

    def is_connected(self) -> bool:
        if self.flag == "inputs":
            if self.get_output():
                return True
        elif self.flag == "outputs":
            if self.get_inputs():
                return True
        return False

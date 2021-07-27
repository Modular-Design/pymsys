from typing import Optional
import inspect
from fastapi import FastAPI, Body, HTTPException, BackgroundTasks, Header


class Server(FastAPI):
    def __init__(self, node):
        super().__init__()

        if inspect.isclass(node):
            self.node_class = node
            self.default = node()
        else:
            self.node_class = node.__class__
            self.default = node

        self.meta = self.default.meta
        self.title = self.meta.get_name()
        self.description = self.meta.get_description()

        @self.get("/config")
        async def get_configuration():
            return self.default.to_dict()

        @self.post("/config")
        async def configure(
                body=Body(
                    ...,
                )):
            instance = self.node_class()
            instance.load(self.default.to_dict())

            if not instance.load(body):
                return
            return instance.to_dict()

        @self.put("/update")
        async def update(
                body=Body(...)
        ):
            instance = self.node_class()
            instance.load(self.default.to_dict())
            if not instance.load(body):
                raise HTTPException(status_code=404, detail="Not Connectable")
            instance.update()
            return instance.to_dict()

    def to_dict(self):
        return dict(meta=self.meta.to_dict())

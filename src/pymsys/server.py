from typing import Optional

from fastapi import FastAPI, Body, HTTPException, BackgroundTasks, Header


class Server(FastAPI):
    def __init__(self, class_name):
        self.default = class_name
        super().__init__()
        obj = self.default()
        self.title = obj.meta.name
        self.description = obj.meta.description

        @self.get("/config")
        async def get_configuration():
            return self.default().to_dict()

        @self.post("/config")
        async def configure(
                body=Body(
                    ...,
                )):
            instance = self.default()
            print(type(body))
            if not instance.load(body):
                return
            return instance.to_dict()

        @self.put("/update")
        async def update(
                body=Body(...)
        ):
            instance = self.default()
            if not instance.load(body):
                raise HTTPException(status_code=404, detail="Not Connectable")
            instance.update()
            return instance.to_dict()


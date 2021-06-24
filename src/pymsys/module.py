from abc import ABC, abstractmethod
from typing import Optional, List

from .connectable import Connectable
from .option import Option
from .interfaces import ISerializer
from fastapi import FastAPI, Body, HTTPException, BackgroundTasks, Header


class Module(FastAPI, ISerializer, ABC):
    def __init__(self,
                 url: Optional[str] = None,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 inputs: Optional[List[Connectable]] = None,
                 outputs: Optional[List[Connectable]] = None,
                 options: Optional[List[Option]] = None,
                 addable_inputs: Optional[bool] = False,
                 addable_outputs: Optional[bool] = False,
                 ram_reserve:Optional[float] = 0.0,):
        super().__init__()
        self.url = url
        self.inputs = inputs
        self.outputs = outputs
        self.options = options
        self.addable_inputs = addable_inputs
        self.addable_outputs = addable_outputs
        self.title = name
        self.description = description
        self.ram_reserve = ram_reserve  # mb

        @self.get("/host")
        async def get_host(host:Optional[str] = Header(None)):
            return {"host": host}

        @self.get("/config")
        async def get_configuration():
            return self.to_json()

        @self.post("/config")
        async def configure(
                body=Body(
                    ...,
                )):
            if not self.load(body):
                return
            return self.to_json()

        @self.post("/input")
        async def add_input():
            if not self.generate_output:
                raise HTTPException(status_code=404, detail="Not Allowed")
            return self.to_json()

        @self.post("/output")
        async def add_output():
            if not self.generate_output:
                raise HTTPException(status_code=404, detail="Not Allowed")
            return self.to_json()

        @self.put("/")
        async def update(
                background_tasks: BackgroundTasks,
                body = Body(...)
        ):
            if not self.load(body):
                raise HTTPException(status_code=404, detail="Not Connectable")
            background_tasks.add_task(self.update, self)
            return self.to_json()

        @self.delete("/input/{id}")
        async def delete_input(id: str):
            if not self.addable_inputs:
                raise HTTPException(status_code=404, detail="Not Allowed")

            for inp in inputs:
                if str(inp.id) == id:
                    del inp
                    return self.to_json()
            raise HTTPException(status_code=404, detail="Not Found")

        @self.delete("/output/{id}")
        async def delete_output():
            if not self.addable_outputs:
                raise HTTPException(status_code=404, detail="Not Allowed")

            for out in outputs:
                if str(out.id) == id:
                    del out
                    return self.to_json()
            raise HTTPException(status_code=404, detail="Not Found")

        @self.delete("/end")
        async def terminate(background_tasks: BackgroundTasks):
            background_tasks.add_task(self.close, self)

        if self.url is not None:
            self.register(self.url)

    def to_json(self) -> dict:
        res = dict()
        res["ram"] = self.ram_reserve
        if self.version:
            res["name"] = self.version
        if self.description:
            res["description"] = self.description
        if self.inputs:
            res["inputs"] = []
            for inp in self.inputs:
                res["inputs"].append(inp.to_json())

        if self.outputs:
            res["outputs"] = []
            for out in self.outputs:
                res["outputs"].append(out.to_json())

        if self.options:
            res["options"] = []
            for opt in self.options:
                res["options"].append(opt.to_json())

        return res

    def load(self, json: dict) -> bool:
        if "url" in json.keys():
            self.url = json["url"]

        if "options" in json.keys():
            options = json["options"]
            for opt in options:
                for option in self.options:
                    if option.id == opt["id"]:
                        if not option.load(opt):
                            return False
                        break

        if "inputs" in json.keys():
            inputs = json["inputs"]
            for inp in inputs:
                for input in self.inputs:
                    if input.id == inp["id"]:
                        if not input.load(inp):
                            return False
                        break

        return True

    def generate_input(self) -> bool:
        if not self.addable_inputs:
            return False
        return True

    def generate_output(self) -> bool:
        if not self.addable_outputs:
            return False
        return True

    def close(self):
        exit(0)

    def register(self, url):
        import socket
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)

        import requests
        requests.post(self.url, data=self.to_json())


    @abstractmethod
    def process(self):
        pass

    def update(self):
        self.process()
        self.register(self.url)

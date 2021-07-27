from typing import Optional

from .interfaces import ISerializer


class Metadata(ISerializer):
    def __init__(self,
                 name: Optional[str] = None,
                 description: Optional[str] = None,
                 **kwargs):
        self.info = kwargs
        self.set_name(name)
        self.set_description(description)

    def get_name(self) -> str:
        return self.info.get("name")

    def set_name(self, name: str) -> None:
        self.info["name"] = name

    def get_description(self) -> str:
        return self.info.get("description")

    def set_description(self, description: str) -> None:
        self.info["description"] = description

    def get_info(self) -> dict:
        return self.info

    def to_dict(self) -> dict:
        return self.info

    def load(self, config: dict) -> bool:
        self.info.update(config)
        return True
from ..interfaces import IGenerator, ILink, ISerializer
from typing import Optional, List, Type, Dict, Any


class Generator(IGenerator):
    def __init__(self,
                 default_class: Type[ILink],
                 parent: Optional[ILink] = None,
                 min_child_limit: Optional[int] = 0,
                 initial_size: Optional[int] = 0,
                 generate_name: Optional[bool] = True,
                 default_config: Optional[dict] = None
                 ):

        self.default_class = default_class

        self.parent = parent

        self.exceptions = []

        self.min_limit = min_child_limit
        self.initial_size = initial_size

        self.generate_name = generate_name
        self.default_config = default_config
        pass

    def set_list(self, child_list: ILink) -> bool:
        self.parent = child_list
        if self.parent is None:
            return True

        keys = list(self.parent.get_childs().keys())

        if not self.exceptions:
            self.exceptions = keys
            self.min_limit = len(keys)

        if self.initial_size > len(keys):
            self.generate(self.initial_size-len(keys), dict())

        return True

    def get_exceptions(self) -> List[str]:
        return self.exceptions

    def generate(self, diff: int, new_config: Dict[str, Any]):
        old_keys = list(self.parent.get_childs().keys())
        new_keys = list(new_config.keys())

        added_keys = list(set(new_keys) - set(old_keys))
        removed_keys = list(set(old_keys) - set(new_keys))

        if diff > 0:
            if len(added_keys) != diff:
                self.generate_child()
            else:
                for i in range(diff):
                    key = added_keys[i]
                    config = new_config[key]
                    self.generate_child(key, config)

        if diff < 0:
            if len(removed_keys) != diff:
                for i in range(abs(diff)):
                    self.remove_child()
            else:
                for i in range(diff):
                    key = removed_keys[i]
                    self.remove_child(key)

        self.sort()


    def generate_child(self, key:Optional[str] = None, config:Optional[dict] = None):
        if config is None:
            config = dict()
        child = self.generate_class(config.get("type"))
        key = self.generate_key(key)

        if isinstance(child, ISerializer):
            if config:
                child.load(config)
            if self.default_config is not None:
                child.load(self.default_config)

        if self.generate_name:
            if hasattr(child, "get_meta"):
                child.get_meta().set_name(key)

        self.parent.add_childs({key: child})

    def remove_child(self, key: Optional[str] = None):
        if key is None:
            self.parent.get_childs().pop(old_keys[-1])
        else:
            self.parent.get_childs().pop(key)

    def generate_class(self, key: Optional[str] = None) -> ILink:
        if key is None:
            return self.default_class()

    def generate_key(self, key: Optional[str] = None) -> str:
        return key

    def sort(self):
        pass

    def key_fits(self) -> bool:
        return True

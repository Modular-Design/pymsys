from .generator import Generator


class CounterGenerator(Generator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_key(self) -> str:
        number = len(self.parent.get_childs())
        for i in range(number):
            key = str(i)
            if not self.parent.get_childs().get(key):
                return key
        return str(number)

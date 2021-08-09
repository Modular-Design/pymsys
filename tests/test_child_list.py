import pytest
from .conftest import parent_testing
from src.pymsys import ChildList, Metadata, Value, Link, Connectable
from src.pymsys import CounterGenerator, Connectable


@pytest.mark.parametrize(
    "test_case",
    [
        ChildList(childs={"1": Link(), "2": Link()}),
        ChildList(childs={"1": Connectable(meta=Metadata(name="Generate Value",
                                                         description="Insert something!", ),
                                           data={"value": 1},
                                           ),
                          "2": Connectable(meta=Metadata(name="Value",
                                                         description="Insert something!", ),
                                           data=Value(),
                                           )})
    ]
)
def test_childlist_parent(test_case):
    assert test_case.parent is None
    parent_testing(test_case)


@pytest.mark.parametrize(
    "test_case",
    [
        ChildList(key_generator=CounterGenerator(default_class=Connectable, initial_size=3))
    ]
)
def test_childlist_generate(test_case):
    assert test_case.parent is None
    keys = list(test_case.childs.keys())
    assert keys == ["0", "1", "2"]

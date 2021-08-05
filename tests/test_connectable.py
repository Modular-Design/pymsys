import pytest
from .conftest import parent_testing
from src.pymsys import Connectable, Metadata, Value

tconnectable_cases = [
    Connectable(meta=Metadata(name="Generate Value",
                              description="Insert something!", ),
                data={"value": 1},
                ),
    Connectable(meta=Metadata(name="Value",
                              description="Insert something!", ),
                data=Value(),
                )
]


@pytest.mark.parametrize(
    "test_case",
    tconnectable_cases
)
def test_connectable_parent(test_case):
    assert test_case.parent is None
    parent_testing(test_case)


@pytest.mark.parametrize(
    "test_case",
    tconnectable_cases
)
@pytest.mark.parametrize(
    "config",
    [
        {"data": {"value": 42}}
    ]
)
def test_load(test_case, config):
    test_case.load(config)
    res = test_case.to_dict()
    for key in config.keys():
        assert res.get(key) == config.get(key)

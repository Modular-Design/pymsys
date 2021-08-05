import pytest
from .conftest import parent_testing
from src.pymsys import Connectable, Metadata, Value, Option

tconnectable_cases = [
    Option(
        title="Insert",
        description="Insert something!",
        default_value=["something"],
    ),
    Option(
        title="Choose One",
        description="Choose one of the folowing!",
        selection=["1", "2", "3"],
    ),
    Option(
        title="Choose Multiple",
        description="Choose one or more of the folowing!",
        selection=["1", "2", "3"],
        single=False,
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
    "test_case, config, success",
    [
        (tconnectable_cases[0], {"value": 2}, True),
        (tconnectable_cases[1], {"value": ["2"]}, True),
        (tconnectable_cases[2], {"value": ["2", "3"]}, True),
        (tconnectable_cases[2], {"value": ["2", "3", "4"]}, False),
    ]
)
def test_load(test_case: Option, config, success):
    load_success = test_case.load(config)
    assert load_success == success
    res = test_case.to_dict()
    for key in config.keys():
        assert (res.get(key) == config.get(key)) == success

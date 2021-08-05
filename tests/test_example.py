import pytest
from .conftest import parent_testing
from src.pymsys import ExampleNode


def test_example_parent():
    test_case = ExampleNode()
    assert test_case.parent is None
    parent_testing(test_case)

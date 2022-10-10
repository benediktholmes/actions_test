import pytest

from src.example_google import module_level_function


def test_module_level_function():
    assert module_level_function('a', 'b')
    assert module_level_function(0,'a')
    assert module_level_function(0)
    assert module_level_function('a')
    assert module_level_function(5)


def test_module_level_function_two():
    with pytest.raises(ValueError):
        assert module_level_function('b', 'b')

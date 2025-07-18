import pytest

from app import add, minus

def test_add():
    assert add(5,7) == 12

def test_minus():
    assert minus(37,7) == 30

def test_divide():
    assert divide(49,7) == 7

import pytest

from app import add

def test_add():
    assert add(5,7) == 12

def test_minus():
    assert minus(14,7) == 7


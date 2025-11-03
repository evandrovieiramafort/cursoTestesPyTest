import pytest

from moduloDez.app import *


@pytest.fixture
def estoque():
    return Estoque()

@pytest.fixture
def produto():
    return Produto("Cabo USB", 5)
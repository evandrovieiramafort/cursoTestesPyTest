import pytest

@pytest.fixture
def lista_exemplo():
    return [1,2,3,4,5]

def test_soma(lista_exemplo):
    assert sum(lista_exemplo) == 15

def test_comprimento(lista_exemplo):
    assert len(lista_exemplo) == 5
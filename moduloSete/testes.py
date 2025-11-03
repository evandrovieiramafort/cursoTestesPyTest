from funcoes import *
import pytest

def test_divisao_erro():
    with pytest.raises(ValueError) as excecao:
        dividir(10,0)
    assert "O divisor não pode ser zero." in str(excecao)
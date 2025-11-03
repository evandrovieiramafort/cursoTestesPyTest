import pytest
from fatorial import fatorial
from moduloQuatro.parametros import parametros_fatorial, variaveis_fatorial


@pytest.mark.parametrize(variaveis_fatorial, parametros_fatorial)
def test_calcula_fatorial(variavel, resultado):
    assert fatorial(variavel) == resultado, "Insira um número positivo!"

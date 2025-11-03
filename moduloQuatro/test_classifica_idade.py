import pytest
from classifica_idade import classifica_idade
from moduloQuatro.parametros import variaveis_classificacao, parametros_classificacao


@pytest.mark.parametrize(variaveis_classificacao, parametros_classificacao)
def test_classifica_idade(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada
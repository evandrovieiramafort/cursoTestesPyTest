import pytest
from moduloDez.tests.parametros import *

@pytest.mark.parametrize(variaveis_teste, parametros_teste)
def test_adicionar_e_verificar_quantidade(estoque, produto, resultado_esperado):
    estoque.adicionar_produto(produto)
    resultado_teste = estoque.verificar_quantidade(produto.nome)
    assert resultado_teste == resultado_esperado

def test_adiciona_produto(estoque, produto):
    estoque.adicionar_produto(produto)
    resultado = estoque.verificar_quantidade(produto.nome)
    assert resultado == 5

@pytest.mark.parametrize(variaveis_teste_invalidos, parametros_teste_invalidos)
def test_adiciona_produto_invalido(estoque, produto_invalido):
    with pytest.raises(ValueError) as excecao:
        estoque.adicionar_produto(produto_invalido)
    assert msg_excecao in str(excecao)

import time
import pytest
from funcoes import *
from parametros import *
from teste_modulo import classifica_idade


@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert soma(2,2) == 4

@pytest.mark.rapido
def test_soma_rapida():
    assert soma(2, 2) == 4

@pytest.mark.lento
def test_multiplicacao_lenta():
    time.sleep(2)
    assert multiplicar(2,2) == 4

@pytest.mark.rapido
def test_multiplicacao_rapida():
    assert multiplicar(2,2) == 4

# ------------------- TESTES DO TESTE ----------------------

@pytest.mark.crianca
@pytest.mark.parametrize(variaveis_classificador, ls_parametros_crianca)
def test_classifica_idade_crianca(idade, resultado):
    assert classifica_idade(idade) == resultado

@pytest.mark.adolescente
@pytest.mark.parametrize(variaveis_classificador, ls_parametros_adolescente)
def test_classifica_idade_adolescente(idade, resultado):
    assert classifica_idade(idade) == resultado

@pytest.mark.adulto
@pytest.mark.parametrize(variaveis_classificador, ls_parametros_adulto)
def test_classifica_idade_adulto(idade, resultado):
    assert classifica_idade(idade) == resultado

@pytest.mark.idoso
@pytest.mark.parametrize(variaveis_classificador, ls_parametros_idoso)
def test_classifica_idade_idoso(idade, resultado):
    assert classifica_idade(idade) == resultado

@pytest.mark.idade_invalida
@pytest.mark.parametrize(variaveis_classificador_invalido, ls_parametros_invalidos)
def test_classifica_idade_erro(idade):
    with pytest.raises(ValueError) as excecao:
        classifica_idade(idade)
    assert "A idade precisa ser um número maior do que 0." in str(excecao)



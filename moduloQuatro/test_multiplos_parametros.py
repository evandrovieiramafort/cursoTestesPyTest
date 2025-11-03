import pytest
from calcula_total import calcula_total

@pytest.mark.parametrize("preco", [10.00, 50.00, 100.00])
@pytest.mark.parametrize("desconto", [0, 0.1, 0.25])
@pytest.mark.parametrize("imposto", [0, 0.05, 0.1])
def test_calcula_total(preco, desconto, imposto):
    # Arrange
    desconto_esperado = preco * desconto
    imposto_esperado = (preco - desconto_esperado) * imposto
    preco_total_esperado = preco - desconto_esperado + imposto_esperado

    # Act
    resultado = calcula_total(preco, desconto, imposto)

    # Assert
    assert resultado == round(preco_total_esperado, 2)


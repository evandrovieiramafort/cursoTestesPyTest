from funcoes import *

def test_eh_positivo_sucesso():
    assert eh_positivo(5) is True
    assert eh_positivo(-5) is False
from funcoes import *

def test_email_valido():
    assert email_valido("exemplo@dominio.com") is True # caso feliz
    assert email_valido("exemplo.com") is False        # caso de falha

def teste_dividir():
    assert dividir(4,2) == 2    # caso feliz
    assert dividir(4,0) is None # caso de falha
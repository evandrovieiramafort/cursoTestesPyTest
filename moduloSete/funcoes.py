"""Vamos considerar uma função chamada dividir que realiza a divisão de dois números, mas lança uma exceção se o divisor
for zero. A tarefa é escrever testes para essa função, verificando se ela lança a exceção esperada quando necessário."""

def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b


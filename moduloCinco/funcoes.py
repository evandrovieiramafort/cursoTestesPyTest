def soma(a,b):
    return a + b

def multiplicar(a,b):
    return a * b

def subtrair(a,b):
    return a - b

def realizar_operacoes(a,b):
    resultado_soma = soma(a,b)
    resultado_subtracao = subtrair(a,resultado_soma) + 10
    resultado_multiplicacao = multiplicar(resultado_subtracao, 2)
    resultado_final = soma(resultado_subtracao, resultado_multiplicacao)

    return resultado_final
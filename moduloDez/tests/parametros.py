from moduloDez.app import Produto

variaveis_teste = "produto, resultado_esperado"
parametros_teste = [
    (Produto("Mouse", 10), 10),
    (Produto("Teclado", 5), 5),
    (Produto("Monitor", 0), 0)
]

variaveis_teste_invalidos = "produto_invalido"
parametros_teste_invalidos = [
    (Produto("Produto inválido 1", -1)),
    (Produto("Produto inválido 2", "a"))
]
msg_excecao = "A quantidade precisa um número maior do que 1."
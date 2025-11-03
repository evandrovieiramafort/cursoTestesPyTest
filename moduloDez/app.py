class Produto:

    def __init__(self, nome: str, quantidade: int):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:

    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto: Produto):
        if not isinstance(produto.quantidade, int) or produto.quantidade < 0:
            raise ValueError("A quantidade precisa um número maior do que 1.")

        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade

    def verificar_quantidade(self, nome_produto: str):
        return self.produtos.get(nome_produto, 0)


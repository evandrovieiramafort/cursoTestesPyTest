def calcula_total(preco, desconto, imposto):
    preco_com_desconto = preco * desconto
    taxa = (preco - preco_com_desconto) * imposto
    total = preco - preco_com_desconto + taxa
    return round(total, 2)

"""Suponha que temos uma função chamada classifica_idade que categoriza a idade de uma pessoa em 'criança', 'adolescente',
'adulto' ou 'idoso'. A tarefa é escrever testes para essa função utilizando markers para diferenciar os testes baseados
 em categorias de idade."""

def classifica_idade(idade):
    if not isinstance(idade, (int, float)) or idade < 0:
        raise ValueError("A idade precisa ser um número maior do que 0.")

    if idade < 13:
        return 'criança'
    elif idade < 20:
        return 'adolescente'
    elif idade < 60:
        return 'adulto'
    else:
        return 'idoso'

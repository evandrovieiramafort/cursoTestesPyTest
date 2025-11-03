def classifica_idade(idade):
    if 0 < idade < 12:
        return "Crianca"
    elif 12 < idade < 18:
        return "Adolescente"
    elif 18 < idade < 60:
        return "Adulto"
    else:
        return "Idoso"


def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

resultado = contador(5)
print(resultado)




numeros = [12, 60, 70, 1, 5]

def cuadrado(n):
     return n ** 2

resultado = map(cuadrado, numeros)
print(list(resultado))


def mayores(n):
    return n>50

resultado = filter(mayores, numeros)
print(list(resultado))
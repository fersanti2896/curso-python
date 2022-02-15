# Funciones lambda

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista de números: {numeros}')

def square(num):
    return num**2

# Función map
print(f'Cuadrado de numeros: {list(map(square, numeros))}')

def valNumPares(num):
    return num % 2 == 0

# Función filter
print(f'Números pares: {list(filter(valNumPares, numeros))}')

# Función lamda
numPar = list(filter(lambda num: num % 2 == 0, numeros))
print(f'Lista de números pares por lambda: {numPar}')

numCuadrado = list(map(lambda num: num ** 2, numeros))
print(f'Lista de números al cuadrado por lambda: {numCuadrado}')
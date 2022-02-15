# Listas de compresión

cadena = 'Hola!'
lista = []

for letra in cadena:
    lista.append(letra)

print(f'Lista: {lista}')

# Haciendo compresión
lista2 = [x for x in range(0, 11)]
print(lista2)

celsius = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fahrenheit = [((temp * (9/5)) + 32) for temp in celsius]

print(f'Grados Celsius: {celsius}')
print(f'Grados Fahrenheit: {fahrenheit}')

# La forma antigüa
gradosF = []
print(f'Grados Fahrenheit: {gradosF}')

for temp in celsius:
    gradosF.append(((9 / 5) * temp) + 32)

print(f'Grados Fahrenheit: {gradosF}')
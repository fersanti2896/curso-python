# Sets, coleccion única y desordenada de elementos, solamente puede haber una representación del mismo objeto

miSet = set()
print(miSet, ' ', type(miSet))

miSet.add(1)
miSet.add(1)
miSet.add(2)

print(miSet)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Valores únicos:', set(numeros))
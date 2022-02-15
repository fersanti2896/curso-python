# Ciclo For

for i in range(10):
    print('Soy:', i)


lista = [1, 2, 3, 2, 1, 3, 5]
suma = 0

for v in lista:
    print('Valor:', v)

for num in range(21):
    if num % 2 == 0:
        print(f'Número par: {num}')
    else:
        print(f'Numero impar: {num}')

for sum in lista:
    suma = suma + sum

print(f'La suma de: {lista} es {suma}')

for carac in 'Hola mundo':
    print(carac)

# Despaquetar tuplas
numeros = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(f'Elementos de lista números {len(numeros)}')

for item in numeros:
    print(item)

for (a, b) in numeros:
    print(a)
    print(b)

dic = {'y1': 1, 'y2': 2, 'y3': 3, 'y4': 4}

for item in dic.items():
    print(item)

for value in dic.values():
    print(value)
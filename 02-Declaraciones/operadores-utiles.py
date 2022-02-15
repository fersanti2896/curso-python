from random import shuffle, randint

lista = list(range(0, 20, 2))
print(lista)

frase = 'Hola soy tu padre.'
for index, value in enumerate(frase):
    print(f'Index: {index} | Valor: {value}')


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = ['a', 'b', 'c', 'd']
lista3 = [100, 200, 300, 400, 450]

for item in zip(lista, lista2, lista3):
    print(f'Parejas: {item}')

nuevaLista = list(zip(lista, lista2, lista3))
print(nuevaLista)

if 'b' in lista2:
    print('Se encontró la b')

print(f'El valor mínimo de {lista3} es {min(lista3)}')
print(f'El valor máximo de {lista3} es {max(lista3)}')

# Para desordenar los valores
print(shuffle(lista))

print('Número aleatorio entre [1, 100]:', randint(1, 100))

nombre = input('Escribe tu nombre: ')
print(nombre)

edad = int(input('Da tu edad: '))
print(type(edad))
print('Tu edad es:', edad)

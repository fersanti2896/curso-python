# Listas, son secuencias ordenadas que guardan una variedad de tipos de objetos, como un arreglo en JS
frutas = ['Naranja', 'Sandía', 'Pera', 'Manzana']
frutas2 = ['Platano', 'Melon']
frutasGeneral = frutas + frutas2

print(frutas)
print('Longitud:', len(frutas))
print('Slicing:', frutas[2:])
print('Nueva lista:', frutasGeneral)

frutasGeneral.append('Coco')
print('Agregando un elemento al final:', frutasGeneral)

frutasGeneral.pop()
print('Eliminando ultimo elemento:', frutasGeneral)

frutasGeneral.pop(1)
print('Eliminando la posicion 1:', frutasGeneral)

frutasGeneral.sort()
print('Lista ordenada:', frutasGeneral)

frutasGeneral.reverse()
print('Lista ordenada al revés:', frutasGeneral)


# Tuplas, son similares a las listas, la diferencia entre las listas es que son inmutables, es decir, sus valores no pueden ser reasignados

tupla = (1, 2, 3)
lista = [1, 2, 3]

print(tupla, ' ', type(tupla))
print(lista, ' ', type(lista))

# Da error
# tupla[0] = 16
# print(tuplas) Imprime: TypeError: 'tuple' object does not support item assignment
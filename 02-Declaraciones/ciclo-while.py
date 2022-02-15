# Ciclo While

x = 0
while (x < 5):
    print(f'El valor actual de x es {x}')
    x = x + 1
else: 
    print(f'x = {x} no es mayor que 5!')

nombre = 'Wendy'

for letra in nombre:
    if (letra == 'y'):
        continue
    print(f'Caracter: {letra}')

print('')
 
for letra in nombre:
    if (letra == 'e'):
        break
    print(f'Caracter: {letra}')
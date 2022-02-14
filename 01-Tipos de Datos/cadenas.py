# Cadenas de texto

nombre = 'Fernando'
nombreCompleto = 'José Fernando Nicolás Santiago.'

print('Me llaman:', nombre, 'Tiene una longitud de:', len(nombre))
print('Mi nombre es:', nombreCompleto, 'Tiene una longitud de:', len(nombreCompleto))

# Indices y Slicing
print('Tomamos la letra é del Nombre Completo:', nombreCompleto[3])
print('Última letra del Nombre Completo:', nombreCompleto[-1])

print('Rango de frase:', nombreCompleto[0:4])
print('Rango de frase:', nombreCompleto[22:-1])

primeras_letras = nombre[:6]
print(primeras_letras + 'da')

x = 'Hola mundo'
print(x)

x = x.upper()
print(x)

x = x.lower()
print(x)

# Separa la cadena en una lista en base al caracter
x = x.split()
print(x)
# Diccionarios, son objetos de clave-valor

diccionario = {
    'Nombre': 'Fernando',
    'Edad': 25, 
    'Profesion:': 'Lic. Computación'
}

print(diccionario)
print(diccionario['Nombre'])

diccionario2 = {
    'Profesiones': ['Ing. Sistemas', 'Programador', 'Ing. Big Data'],
    'Lenguajes': ['C', 'Java', 'JavaScript', 'Python']
}

print(diccionario2)
print(diccionario2['Lenguajes'])
print(diccionario2.keys())
print(diccionario2.values())
print(diccionario2.items())

# Funciones

def saludo(nombre, edad):
    return f'Hola: {nombre}, Tu edad es: {edad}'

name = input('Da tu nombre: ')
age  = int(input('Da tu edad: '))

print(saludo(name, age))


def suma(num1 = 0, num2 = 0):
    suma = num1 + num2
    return f'La suma es: {suma}'

print(suma(2))
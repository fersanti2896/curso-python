# Argumentos (*args, **kwargs) -> *args =  tupla, **kwards = diccionario

def func(*args):
    return sum(args) * 0.05

print(f'La suma es: {func(40, 50, 700)}')

def func2(**kwargs):
    if 'fruit' in kwargs:
        return 'Mi fruta es {}'.format(kwargs['fruit'])
    else: 
        return 'No hay fruta'

print(func2(fruit = 'Naranja', vegetables = 'Zanahoria', bread = 'Bolillo'))

def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    return 'Me gustaría {} de {}'.format(args[3], kwargs['eat'])

print(func3(10, 20, 30, vetetables = 'Papa', eat = 'Tacos de cecina'))
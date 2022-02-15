# Herencia

class Animal():
    def __init__(self):
        print('Animal Creado')

    def infoAnimal(self):
        print('Soy un Animal')

    def comer(self):
        print('Estoy comiendo')


class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Perro Creado')

    def infoAnimal(self):
        print('Soy un Perro')

perro1 = Perro()
perro1.infoAnimal()
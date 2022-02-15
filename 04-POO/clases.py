
class Dog():
    def __init__(self, raza, nombre, color, puntos):
        # Atributos
        self.raza = raza
        self.nombre = nombre
        self.color = color

        # Valor booleano True/False
        self.puntos = puntos
    
huskyi = Dog('Huskyi', 'Juanito', 'Café', False)
print(huskyi)
    
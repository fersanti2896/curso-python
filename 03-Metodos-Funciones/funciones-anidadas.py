# Funciones Anidades

# Global
name = 'VARIABLE GLOBAL'

def saludo():
    # Enclosing
    name = 'Fernando Nicolás'

    def hola():
        # Local
        name = 'Variable local'
        print(f'Hola {name}')
    
    hola()

saludo()
# Manejo de errores

try:
    # Intentamos correr este código
    # Puede haber errores
    result = 10 + '10'
    print(f'El valor es: {result}')
except:
    print('Parece que hay un error, escribe correctamente las variables!')
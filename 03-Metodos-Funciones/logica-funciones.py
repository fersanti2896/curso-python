# Logica en funciones

def verNumParLista(lista):
    for num in lista:
        if num % 2 == 0:
            return True
        else:
            pass
    
    return False

print(verNumParLista([1, 2, 3, 4, 6]))
import random

def generar_vectores():
    vector1 = [random.randint(1, 10) for _ in range(3)]
    vector2 = [random.randint(1, 10) for _ in range(3)]
    return vector1, vector2

def calcular_suma(vector1, vector2):
    return sum(vector1) + sum(vector2)

def juego_adivina_la_suma():
    print("¡Bienvenido al juego 'Adivina la suma'!")
    vector1, vector2 = generar_vectores()
    suma = calcular_suma(vector1, vector2)
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    intento = int(input("¿Cuál crees que es la suma de todos los números de ambos vectores? "))
    if intento == suma:
        print("¡Correcto! Has adivinado la suma.")
    else:
        print("Incorrecto. La suma real es:", suma)
juego_adivina_la_suma()

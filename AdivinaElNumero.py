import random

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    print("¡Intenta adivinarlo!")

    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            intento = int(input("\nIngresa tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1
        if intento < numero_secreto:
            print("¡Demasiado bajo! Intenta de nuevo.")
        elif intento > numero_secreto:
            print("¡Demasiado alto! Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivina_el_numero()

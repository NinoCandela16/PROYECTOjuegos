import random
modalidad = input("¿Quieres jugar contra la computadora o de a dos jugadores? (computadora/dos): ").lower()
if modalidad == "computadora":
    opciones = ["piedra", "papel", "tijera"]
    while True:
        usuario = input("Elije piedra, papel o tijera: ").lower()
        computadora = random.choice(opciones)
        print(f"El rival elige: ", {computadora})
        if usuario == computadora:
            print("Es un empate")
        elif usuario == "piedra" and computadora == "tijera":
            print("¡Ganaste!")
        elif usuario == "papel" and computadora == "piedra":
            print("¡Ganaste!")
        elif usuario == "tijera" and computadora == "papel":
            print("¡Ganaste!")
        elif usuario == "tijera" and computadora == "piedra":
            print("Perdiste")
        elif usuario == "piedra" and computadora == "papel":
            print("Perdiste")
        elif usuario == "papel" and computadora == "tijera":
            print("Perdiste")
        else:
            print("Opcion no valida, elige una correcta")
        volver_a_jugar = input("¿Quieres volver a jugar? (si/no): ").lower()
        if volver_a_jugar != "si":
            break
elif modalidad == "dos":
    opciones = ["piedra", "papel", "tijera"]
    while True:
        usuario1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
        if usuario1 not in opciones:
            print("Opción no válida, elige una correcta (piedra, papel o tijera).")
            continue  
        usuario2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
        if usuario2 not in opciones:
            print("Opción no válida, elige una correcta (piedra, papel o tijera).")
            continue  
        print(f"Jugador 1 elige: {usuario1}")
        print(f"Jugador 2 elige: {usuario2}")
        if usuario1 == usuario2:
            print("Es un empate")
        elif usuario1 == "piedra" and usuario2 == "tijera":
            print("¡Jugador 1 gana!")
        elif usuario1 == "papel" and usuario2 == "piedra":
            print("¡Jugador 1 gana!")
        elif usuario1 == "tijera" and usuario2 == "papel":
            print("¡Jugador 1 gana!")
        else:
            print("¡Jugador 2 gana!")

        volver_a_jugar = input("¿Quieren volver a jugar? (si/no): ").lower()
        if volver_a_jugar != "si":
            break
else:
    print("Opción no válida, elige 'computadora' o 'dos'.")

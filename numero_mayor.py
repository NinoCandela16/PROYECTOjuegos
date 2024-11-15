import random

while True:
    
    numeros = [random.randint(1, 100) for _ in range(5)]
    mayor = max(numeros) 
    print("Números generados:", numeros)  
    
    adivinanza = int(input("Adivina el número mayor: "))
    
    if adivinanza == mayor:
        print("¡Correcto! El número mayor es:", mayor)
    else:
        print("Incorrecto. El número mayor era:", mayor)

    if input("¿Quieres jugar otra vez? (si/no): ").lower() != 'si':
        print("¡Gracias por jugar, espero que vuelvas!")
        break

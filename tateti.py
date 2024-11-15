tateti=[["00", "01", "02"],
        ["10", "11", "12"],
        ["20", "21", "22"],]
empate=True
tiposdeficha=("X", "O", "X", "O", "X", "O", "X", "O", "X", "")

ciclo=0
while ciclo < 9: #Etapa de colocar las fichas
    datos=False
    while datos == False: 
        for i in range(3):
            print(tateti[i])
        posicioni=int(input(f"Escribe el primer numero de la posicion donde quieres poner {tiposdeficha[ciclo]}: "))
        while 0 > posicioni or posicioni > 2:
            print("El valor escrito no es valido")
            posicioni=int(input(f"Escribe el primer numero de la posicion donde quieres poner {tiposdeficha[ciclo]}: "))
        posicionj=int(input(f"Escribe el segundo numero de la posicion donde quieres poner {tiposdeficha[ciclo]}: "))
        while 0 > posicionj or posicionj > 2:
            print("El valor escrito no es valido")
            posicionj=int(input(f"Escribe el segundo numero de la posicion donde quieres poner {tiposdeficha[ciclo]}: "))
        if tateti[posicioni][posicionj] == "X" or tateti[posicioni][posicionj] == "O":
            print("La posicion que intentas marcar ya esta ocupada")
        else:
            datos=True
    tateti[posicioni][posicionj]=tiposdeficha[ciclo]
    
    for j in range(3): #Comprueba si las columnas y filas hay 3 X o O 
        if tateti[j][0] == "X" and tateti[j][1] == "X" and tateti[j][2] == "X":
            for x in range(3):
                print(tateti[x])
            print("X gano la partida")
            ciclo+=10
            empate=False
        if tateti[j][0] == "O" and tateti[j][1] == "O" and tateti[j][2] == "O":
            for x in range(3):
                print(tateti[x])
            print("O gano la partida")
            ciclo+=10
            empate=False
        if tateti[0][j] == "X" and tateti[1][j] == "X" and tateti[2][j] == "X":
            for x in range(3):
                print(tateti[x])
            print("X gano la partida")
            ciclo+=10
            empate=False
        if tateti[0][j] == "O" and tateti[1][j] == "O" and tateti[2][j] == "O":
            for x in range(3):
                print(tateti[x])
            print("O gano la partida")
            ciclo+=10
            empate=False

    if tateti[0][0] == "X" and tateti[1][1] == "X" and tateti[2][2] == "X": #Comprueba si en la pediente mayor hay 3 X o O 
        for x in range(3):
            print(tateti[x])
        print("X gano la partida")
        ciclo+=10
        empate=False
    if tateti[0][0] == "O" and tateti[1][1] == "O" and tateti[2][2] == "O":
        for x in range(3):
            print(tateti[x])
        print("O gano la partida")
        ciclo+=10
        empate=False
    
    if tateti[0][2] == "X" and tateti[1][1] == "X" and tateti[2][0] == "X": #Comprueba si en la pediente menor hay 3 X o O 
        for x in range(3):
            print(tateti[x])
        print("X gano la partida")
        ciclo+=10
        empate=False
    if tateti[0][2] == "O" and tateti[1][1] == "O" and tateti[2][0] == "O":
        for x in range(3):
            print(tateti[x])
        print("O gano la partida")
        ciclo+=10
        empate=False
    
    ciclo+=1

if empate == True:
    for x in range(3):
        print(tateti[x])
    print("Hay un empate")

fila =5
columna = 0
espai = fila
for files in range(0, fila):
    espai = espai -1
    columna = columna +1
    for espais in range (0,espai):
        print(" ", end= " ")
    for columnes in range (0,columna):
        print( "*", end= " ")
    print(" ")
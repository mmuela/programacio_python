espai = 0
fila = 5
columna = fila
for files in range(0, fila):
    columna = columna -1
    espai = espai + 1
    for espais in range (1,espai):
        print( " ", end= " ")
    for columnes in range (0, columna+1):
        print( "*", end= " ")
    print(" ")
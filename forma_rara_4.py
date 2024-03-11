files=5
columnes=5
for fila in range(0,files):
    columnes=columnes-1
    for columna in range (1,columnes+1):
        print(" ", end=" ")
    for espai in range(0,fila+1):
        print("*",end=" ")
    print("")
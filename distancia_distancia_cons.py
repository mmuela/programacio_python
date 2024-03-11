def distancia_cons(cons,distancia,amplada):
    if cons==1:
        distancia_entre_cons=amplada
    else:
        distancia_entre_cons=(distancia*(cons-1))+(amplada*(cons-2))
    print(distancia_entre_cons)

cons=0
while cons<1:
    cons=int(input("nº de cons ="))
    if cons<1:
        print("no poden haver cons negatius")
distancia=0
while distancia>30 or distancia<10:
    distancia=int(input("distancia entre cons (entre 10 i 30 m)="))
    if distancia>30 or distancia<10:
        print("entre 10 i 30")
amplada=0
while amplada>50 or amplada<10:
    amplada=int(input("distancia entre cons (entre 10 i 50 cm)="))
    if amplada>50 or amplada<10:
        print("entre 10 i 50")
amplada=amplada/100
distancia_cons(cons,distancia,amplada)

    
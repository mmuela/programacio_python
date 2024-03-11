from math import*
dia=int(input("dia de naixement = "))
mes=int(input("mes de naixement = "))
anyy=int(input("any de naixement = "))
if dia>31 or mes>12 or dia<1 or mes<1 or anyy>9999 or(dia>29 and mes==2):
    print("error")
else:
    desena_dia=dia//10
    unitat_dia=dia%10
    desena_mes=mes//10
    unitat_mes=mes%10
    unitat_any=anyy%10
    miler_any=anyy//1000
    centena_any=(anyy//100)-(miler_any*10)
    desena_any=(anyy//10)-(centena_any*10)-(miler_any*100)
    s=desena_dia+unitat_dia+desena_mes+unitat_mes+unitat_any+miler_any+centena_any+desena_any
    sumadefinitiva=(s%10)+(s//10)
    print("el teu nombre del tarot es: ",sumadefinitiva)
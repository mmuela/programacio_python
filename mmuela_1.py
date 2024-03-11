#mmuela_1.py
n=int(input("nombre traballadors="))
i=1
while i<n:
    sou=float(input("sou de la persona ="))
    pagar=0
    guanys=0
    if sou<10000:
        pagar=0.05*sou
        print("paga",pagar,"€")
        print("sou restnant =",(sou-pagar))
    elif sou <20000:
        pagar=sou*0.15
        print("paga",pagar,"€")
        print("sou restnant =",(sou-pagar))
    elif sou<35000:
        pagar=sou*0.2
        print("paga",pagar,"€")
        print("sou restnant =",(sou-pagar))
    elif sou<60000:
        pagar=sou*0.3
        print("paga",pagar,"€")
        print("sou restnant =",(sou-pagar))
    else:
        pagar=sou*0.45
        print("paga",pagar,"€")
        print("sou restnant =",(sou-pagar))
    i=i+1
    

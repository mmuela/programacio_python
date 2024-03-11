#mmuela_3.py
def gelat_avellana():
    print("preu 2,25")
    monedes_2=int(input("monedes de 2 euros ="))
    monedes_1=int(input("monedes de 1 euro ="))
    monedes_50=int(input("monedes de 50 ctms ="))
    monedes_20=int(input("monedes de 20 ctms ="))
    monedes_5=int(input("monedes de 5 ctms ="))
    x=(monedes_2*2)+(monedes_1)+(monedes_50*0.5)+(monedes_20*0.2)+(monedes_5*0.05)
    if x>=2.25:
        canvi=x-2.25
        retornar_2=canvi//2
        retornar_1=(canvi-retornar_2)//1
        retornar_50=((canvi-retornar_2*2)-retornar_1)//0.5
        retornar_20=((canvi-retornar_2*2)-retornar_1-(retornar_50*0.5))//0.2
        retornar_5=((canvi-retornar_2*2)-retornar_1-(retornar_50*0.5)-(retornar_20*0.2))//0.05
        print("es retornen",canvi,"€ en:",retornar_2,"monedes de 2€,", retornar_1,"monedes de 1€,",retornar_50,"monedes de 50 ctms,",retornar_20," monedes de 20 ctms i",retornar_5," monedes de 5 ctms")
    else:
        print("no hi ha prou diners, torni a intentar")
def pastis_ametlla():
    print("preu 1,75 €")
    monedes_2=int(input("monedes de 2 euros ="))
    monedes_1=int(input("monedes de 1 euro ="))
    monedes_50=int(input("monedes de 50 ctms ="))
    monedes_20=int(input("monedes de 20 ctms ="))
    monedes_5=int(input("monedes de 5 ctms ="))
    x=(monedes_2*2)+(monedes_1)+(monedes_50*0.5)+(monedes_20*0.2)+(monedes_5*0.05)
    if x>=1.75:
        canvi=x-1.75
        retornar_2=canvi//2
        retornar_1=(canvi-retornar_2)//1
        retornar_50=((canvi-retornar_2*2)-retornar_1)//0.5
        retornar_20=((canvi-retornar_2*2)-retornar_1-(retornar_50*0.5))//0.2
        retornar_5=((canvi-retornar_2*2)-retornar_1-(retornar_50*0.5)-(retornar_20*0.2))//0.05
        print("es retornen",canvi,"€ en:",retornar_2,"monedes de 2€,", retornar_1,"monedes de 1€,",retornar_50,"monedes de 50 ctms,",retornar_20," monedes de 20 ctms i",retornar_5," monedes de 5 ctms")
    else:
        print("no hi ha prou diners, torni a intentar")
x=False
while x==False:
    print("menú:")
    print("1. gelat d'avellana")
    print("2. pastis d'atmetlla")
    print("3. soritda")
    a=int(input("que li ve mes de gust?"))
    if a==1:
        gelat_avellana()
    elif a==2:
        pastis_ametlla()
    else:
        print("gracies per la compra")
        x=True

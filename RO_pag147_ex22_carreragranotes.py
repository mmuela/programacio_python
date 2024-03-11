#RO_pag147_ex22_carreragranotes.py
from random import*
r1=0
r2=0
r3=0
while r1<20 and r2<20 and r3<20:
    tirada_1=randint(0,5)
    tirada_2=randint(0,5)
    tirada_3=randint(0,5)
    if tirada_1==0:
        r1=r1+1
    elif tirada_1==2:
        r1=r1+0.5
    elif tirada_1==3:
        r1=r1
    elif tirada_1==4:
        r1=r1-0.5
    elif tirada_1==5:
        r1=r1-1
    if tirada_2==0:
        r2=r2+1
    elif tirada_2==2:
        r2=r2+0.5
    elif tirada_2==3:
        r2=r2
    elif tirada_2==4:
        r2=r2-0.5
    elif tirada_2==5:
        r2=r2-1
    if tirada_3==0:
        r3=r3+1
    elif tirada_3==2:
        r3=r3+0.5
    elif tirada_3==3:
        r3=r3
    elif tirada_3==4:
        r3=r3-0.5
    elif tirada_3==5:
        r3=r3-1
print("rana 1",r1)
print("rana 2",r2)
print("rana 3",r3)


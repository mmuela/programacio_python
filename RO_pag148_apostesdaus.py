#RO_pag148_apostesdaus.py
from random import*
import time
n=int(input("nº d llançaments: "))
i=1
d=0
while i<=n:
    ll=randint(1,6)
    if ll==1:
        d=d+1
        print("ha sorit un 1, guanya 1$")
        print("dinerro =" ,d)
    elif ll==6:
        d=d+5
        print("ha sorit un 6, guanya 5$")
        print("dinerro =" ,d)
    else:
        d=d-2
        print("ha sorit un",ll,"perd 2$")
        print("dinerro =" ,d)
    time.sleep(2)
    i=i+1
print("dinerro final :",d)
if d>0:
    print("felicitats, has tingut molta sort")
else:
    print("savies que no havies de jugar, no es el teu dia de sort")
#RO_pag147_ex014_while.py
from math import*
import time
d=float(input("diners ="))
n=int(input("nombre articles ="))
i=0
while i<n:
    a=float(input("preu article ="))
    if a<=d:
        d=d-a
        print("it is purchaseable")
        if a<=d:
            u=d//a
            print("es poden comprar" ,u,"articles")
    else:
        print("you can't afford it")
    i=i+1
time.sleep(1)
print("this is the eeend")
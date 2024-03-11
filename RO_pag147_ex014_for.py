#RO_pag147_ex014_for.py
from math import*
a=[10,20,30,40]
d=int(input("do ju gaf moni? gou max?"))
i=0
for n in a:
    i=i+1
    if d>=n:
        u=d//n
        print("pots comprar" ,u, "unitats de l'article",i,)
    else :
        print("im sorry man u r poor")
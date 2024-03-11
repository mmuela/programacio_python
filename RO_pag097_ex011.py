#RO_pag097_ex011.py
from math import*
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))

modul_a = sqrt(pow(a,2)+pow(b,2))
modul_b = sqrt(pow(c,2)+pow(d,2))
print("el punt mes aprop del centre és:")
if modul_a<modul_b:
    print("el punt 1")
elif modul_a>modul_b:
    print("el punt b")
else:
    print("estàn igual d'aprop")
#RO_pag096_ex07.py
from math import*
p=float(input("insereixi 1 per pasar de Fº a Cº, o 2 per pasar de Cº a Fº =" ))
if p==1:
    t=float(input("temperatura en Fº ="))
    c=5/9*(t-32)
    print("temperatura en Cº =",c)
elif p==2:
    t=float(input("temperatura en Cº ="))
    f=32+9*t/5
    print("temperatura en fº =",f)
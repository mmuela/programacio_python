#RO_pag096_ex06.py
from math import *
kwh=float(input("kw/h consumits = "))
preu_kwh=float(input("preu per kw/h = "))

preu=preu_kwh*kwh
if kwh>700:
    preu=preu*1.05
print(preu)
        
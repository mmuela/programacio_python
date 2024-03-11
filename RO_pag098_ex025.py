#RO_pag098_ex025.py
from math import*
q=float(input("kilograms comprats:"))
if q<3:
    print("2,4$")
elif q>=3 and q<6:
    print("2,3$")
elif q>=6 and q<10:
    print("2,1$")
else:
    print("1,85$")

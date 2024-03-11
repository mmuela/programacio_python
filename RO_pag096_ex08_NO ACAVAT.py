#RO_pag096_ex08.py
from math import*
nj1=float(input("1a nota de joan ="))
nj2=float(input("2a nota de joan ="))
nj3=float(input("3a nota de joan ="))
np1=float(input("1a nota de pere ="))
np2=float(input("2a nota de pere ="))
np3=float(input("2a nota de pere ="))

if nj1==nj2:
    if nj2==nj3 or nj2>nj3:
        nota_j1=nj1
        nota_j2=nj1
    else:
        nota_j1=nj3
        nota_j2=nj1
elif nj2==nj3:
    if nj2>nj1:
        nota_j1=nj2
        nota_j2=n3
    else:
        nota_j1=nj1
        nota_j2=nj2
elif nj1
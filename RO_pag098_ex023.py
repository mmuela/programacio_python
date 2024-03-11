#RO_pag098_ex023.py
from math import*
n1=float(input("nota 1 ="))
n2=float(input("nota 2 ="))
n3=float(input("nota 3 ="))

if n1<n2:
    if n3<n1:
        print(n3)
        print(n1)
        print(n2)
    elif n2<n3:
        print(n1)
        print(n2)
        print(n3)
    elif n3<n2:
        print(n1)
        print(n3)
        print(n2)
elif n2<n1:
    if n3<n2:
        print(n3)
        print(n2)
        print(n1)
    elif n1<n3:
        print(n2)
        print(n1)
        print(n3)
    elif n3<n1:
        print(n2)
        print(n3)
        print(n1)

#RO_pag097_ex09.py
from math import*
n1=float(input("n1="))
n2=float(input("n2="))
n3=float(input("n3="))

if n1>n2 and n1>n3:
    print("la mes gran és n1",n1)
elif n2>n1 and n2>n3:
    print("la mes gran és n2",n2)
elif n3>n1 and n3>n2:
    print("la mes gran és n3",n3)
if n1<n2 and n1<n3:
    print("la mes petita és n1",n1)
elif n1>n2 and n2<n3:
    print("la mes petita és n2",n2)
elif n3<n2 and n1>n3:
    print("la mes petita és n3",n3)

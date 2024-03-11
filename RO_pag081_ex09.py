#RO_pag81_ex09.py
from math import *

a=float(input("a ="))
b=float(input("b ="))

c=float(input("c ="))
d=float(input("d ="))

x=sqrt(pow((c-a),2)+(pow((d-b),2)))
y=sqrt(pow(c,2)+pow(d,2))
z=sqrt(pow(a,2)+pow(b,2))
t=(x+y+z)/2
s=sqrt(t*(t-x)*(t-y)*(t-z))

print(s)
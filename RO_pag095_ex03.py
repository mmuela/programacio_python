#RO_pag095_ex03.py
from math import *
x=4
y=4
z=5

d1=sqrt(pow(x,2)+pow(y,2))
d2=sqrt(pow(x,2)+pow(z,2))
d3=sqrt(pow(y,2)+pow(z,2))

print("diagonal 1 es la diagonal amplada-altura")
print("diagonal 1 es la diagonal amplada-profunditat")
print("diagonal 3 es la diagonal altura profunditat")
if d1==d2 and d2 == d3:
    print("totes iguals",d1)
elif d1==d2 and d1>d3:
    print("les mes grans son diagonal 1 i 2",d1,)
elif d1==d2 and d1<d3:
    print("la diagonal mes gran es la 3",d3)
elif d1==d3 and d1>d2:
    print("les mes grans son diagonal 1 i 3",d1,)
elif d1==d3 and d1<d2:
    print("la mes gran és d2",d2)
elif d2==d3 and d2>d1:
    print("les mes grans son diagonal 2 i 3",d2,)
elif d2==d3 and d2<d1:
    print("la mes gran és d1",d1)
elif d1>d2>d3:
    print("la mes gran es la diagonal 1", d1)
elif d2>d1>d3:
    print("la mes gran es la diagonal 2",d2)
elif d3>d1>d2:
    print("la mes gran es la diagonal 3",d3)

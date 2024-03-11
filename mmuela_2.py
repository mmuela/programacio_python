#mmuela_2.py
from math import*
x=int(input("any ="))
a=x%19
b=x%14
c=x%7
d=(19*a+24)%30
e=(2*b+4*c+6*d+5)%7
f=22+d+e

if f>31:
    print("diumenge de pascua caurà o ha caigut en",(f-31),"d'abril")
else:
    print("diumenge de pascua caurà o ha caigut en",f,"de març")
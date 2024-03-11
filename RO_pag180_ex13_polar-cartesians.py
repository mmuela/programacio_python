#RO_pag180_ex13_polar-cartesians.py
from math import*
import time
def polar(x,y):
    r=sqrt(x**2+y**2)
    t=atan(x/y)
    t=180/pi*t
    return (r,t)
def cartesians(r,t):
    t=t*pi/180
    x=r*cos(t)
    y=r*sin(t)
    return x,y
i=False
while i==False:
    print("menú")
    time.sleep(0.3)
    print("1. pasar de cartesians a polars")
    time.sleep(0.3)
    print("2. pasar de polars a cartesians")
    time.sleep(0.3)
    print("3. exit")
    time.sleep(0.3)
    p=int(input("la seva elecció: "))
    if p==1:
        print("")
        x=float(input("cordenades al eix x (m)="))
        y=float(input("cordenades al eix y (m)="))
        r,t = polar(x,y)
        print(r, "metres en ",t,"graus")
    elif p==2:
        print("")
        r=float(input("llargada del vector posició (m)="))
        t=float(input("angle del vectro sobre el pla ="))
        x,y = cartesians(r,t)
        print(x,",",y)
    elif p==3:
        print("")
        print("gracies apa adeu siau")
        i=True
    else:
        print("")
        print("no bro, es o 1 o 2 o 3")
        time.sleep(0.5) 
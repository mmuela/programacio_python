#mmuela_1_febrer.py
from math import*
from random import*
def f(a):
    y=4+sin(a)
    return y
def f2(a):
    y=4+230*sin(a)
    return y
a=0
for i in range(1,8+1):
    a=a+45
    a=a*pi/180
    y=f(a)
    y2=f2(a)
    a=a*180/pi
    print(a,"f(a) =" ,y)
    print(a,"f2(a)=" ,y2)
#tots els valors de y no donaran sempre positiu, perque quan el sinus d'alfa es negatiu, tot i ser menor a 1, al multiplicarse per 230 i sumarli 4, f(a) dona negatiu

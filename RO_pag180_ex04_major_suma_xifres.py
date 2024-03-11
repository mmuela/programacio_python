#RO_pag180_ex4_sumadesumes.py
from math import*
from random import*
def suma_xifres(n):
    u=n%10
    d=n//10
    suma=d+u
    return suma
i=1
y=0
p=0
while i<11:
    n=randint(1,99)
    suma = suma_xifres(n)
    if suma>y:    
        y=suma
        p=n
    print(n," = ",suma)
    i=i+1
print("el que suma mes és: ",p," que suma ",y)
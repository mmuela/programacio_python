#RO_pag180_ex21_triangular.py
from math import*
def whille(n,y):
    i=0
    while i<=n:
        y=y+i
        i=i+1
    return y
def forr(n,y):
    for i in range(1,n+1):
        y=y+i
    return y
n=int(input("nombre ="))
y=0
a=int(input("amb for insert 1; amb while insert 2: "))
if a==1:
    y = forr(n,y)
elif a==2:
    y =whille(n,y)
print(y)
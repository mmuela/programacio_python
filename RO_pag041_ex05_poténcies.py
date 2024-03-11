#RO_page41_ex05_poténcies.py
import time

n=int(input("n= "))
v=0
x=0
h=0

while h<=n:
    n1=v
    n2=v+1
    x=((n1**n1)+(n2**n2))
    h=x
    v=v+1
    x=x+1
    print(x,v)
    time.sleep(1)
    

    
#RO_pag180_ex01_divisors.py
from math import*
def divisors(n):
    j=0
    i=0
    for i in range(1,n+1):
        if n%i==0:
            print(i, "es divisor de",n)
            j=j+1
    if j==2:
        print(n, "és un nombre primer")
    return(j)
n=int(input("n ="))
divisors(n)
for k in range (1,101):
    j=divisors(n)
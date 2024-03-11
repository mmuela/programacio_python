#RO_pag104_sumaquadrats.py
from math import*
n=int(input("n ="))
s=0
i=1
while i<=n:
    s=s+pow(i,2)
    i=i+1
print(s)
#RO_pag146_ex02.py
from math import*
n=int(input("nº objectes="))
i=1
menor10=0
major20=0
e10i20=0
while i<n:
    print("pes",i,"=",end="")
    pes=int(input())
    if pes<10:
        menor10=menor10+1
    elif pes>10 and pes<20:
        e10i20=e10i20+1
    else:
        major20=major20+1
    i=i+1
print("nombre d'objectes menors a 10k = ",menor10)
print("nombre d'objectes menors a 20k i majors de 10k = ",e10i20)
print("nombre d'objectes majors a 20k = ",major20)
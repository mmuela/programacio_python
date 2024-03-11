#RO_pag146_ex01.py
from math import*
n=int(input("n paquets="))
i=0
p=0
pg=0
pp=10^99
sp=0
while i<n:
    p=float(input("pes ="))
    if p>pg:
        pg=p
    if p<pp:
        pp=p
    sp=sp+p
    i=i+1
print ("pes maxim=",pg)
print("pes minim =", pp)
print ("mitjana=" ,(sp/i))
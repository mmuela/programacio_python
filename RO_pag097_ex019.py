#RO_pag097_ex019.py
from math import*
print("1=afavor, 0=en contra")
j1=int(input("j1 ="))
j2=int(input("j2 ="))
j3=int(input("j3 ="))
if j1>1 or j2>1 or j3>1:
    print("error")
elif j2==1 and j3==1:
    print("continua")
elif j1==1 and j3==1:
    print("continua")
elif j1==1 and j2==1:
    print("continua")
else :
    print("eliminat")
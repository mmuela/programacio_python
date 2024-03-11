#RO_pag095_ex04.py
from math import*
n=int(input("nombre de dues xifres="))
desenes=n//10
unitats=n%10
k=desenes+unitats
if k%2==0:
    print("parell",k)
else :
    print("imparell",k)
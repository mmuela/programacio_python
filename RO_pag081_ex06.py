#RO_pag081_ex06.py
from math import*
e=float(input("nota examen ="))
t1=float(input("nota de la 1a tasca ="))
t2=float(input("nota de la segona tasca ="))
t3=float(input("nota de la 3a tasca ="))
l=float(input("nota de la lliçó ="))

examen=e*0.7
traballs=((t1+t2+t3)/3)*0.2
lliçons=l*0.1
nota=examen+traballs+lliçons
nota=nota*10
print(nota)
#mmuela_3c.py
from math import*
h=400
x=750
y=1250
t1=15
t2=35
Ce=4.187#calor especific de l'aigua
t=t2-t1#diferencia de temperatura
h=h/1000#pasar de milimetres a metres
x=x/1000#pasar de milimetres a metres
y=y/1000#pasar de milimetres a metres
Pc=47.79#podr calorific del combustible en MJ/kg
Eu=Ce*t*x*y*h*1000#formula
Ee=Eu/0.8#energia sortida / rendiment
mcombustible=Eu/Pc
preu=12.95/12.5#euros / kg (preu i massa d'una bombona)
preu_minim=preu*mcombustible
print("preu minim de combustible=",preu_minim)
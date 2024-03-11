#mmuela_3.py
from math import*
h=float(input("alçada banyera en mm ="))
x=float(input("amplada banyera en mm ="))
y=float(input("profunditat banyera en mm ="))
t1=float(input("temperatura inicial de l'aigua en Cº ="))
t2=float(input("temperatura final de l'aigua en Cº ="))
Pc=4.187#poder calorific de l'aigua
t=t2-t1#diferencia de temperatura
h=h/1000#pasar de milimetres a metres
x=x/1000#pasar de milimetres a metres
y=y/1000#pasar de milimetres a metres
Eu=Pc*t*x*y*h*1000#formula
print (Eu,"KJ")
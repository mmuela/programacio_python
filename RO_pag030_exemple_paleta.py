# RO_page030_exemple_paleta.py

c = float(input("c = "))
t = float(input("t = "))
d = float(input("d = "))

if c<=40:
    p = (t * c) - d

else: p = ((40 * t) + (c - 40) * 1.5) - d

print("sou net =",p,)
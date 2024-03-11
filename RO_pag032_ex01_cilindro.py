# RO_page032_ex01_cilindro.py
radi = float(input(" radi = "))
altura = float(input(" altura ="))
pi = 3.1416
if altura > radi :
    volum = pi * radi * radi * altura
    print("volum = ", volum, "cm3")
else :
    area = (2 * pi * radi * (altura + radi))
    print(" area = " , area, " cm2")
# RO_page032_ex02.py
kw_h = float(input(" kw/h = "))
preu = float(input(" preu del kw/h = "))

cost = preu * kw_h

if kw_h > 700 :
    cost = 700 + (kw_h-700) * 1.05

print(" cost = " ,cost, "€")
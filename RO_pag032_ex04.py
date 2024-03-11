# RO_page032_ex04.py
x = float(input("llargada = "))
y = float(input("alçada = "))
z = float(input("prfunditat = "))

d1 = ((x **2) + (y **2)) ** 0.5
d2 = ((x **2) + (z **2)) ** 0.5
d3 = ((y **2) + (z **2)) ** 0.5

if d1>d2 and d1>d3:
    print("diagonal mes gran es = ",d1)

if d2>d1 and d2>d3:
    print("diagonal mes gran es = ",d2)

if d3>d1 and d3>d2:
    print("diagonal mes gran es = ",d3)
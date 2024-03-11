# RO_page032_ex03.py
codi = int(input("insereixi codi, 1 per Fº-->Cº; 2 per Cº-->Fº =")) 
t = float(input("temperatura = "))
if codi == 1 :
    c = (5 / 9) * (t - 32)
    print("temperatura = ", c," Cº")

if codi == 2:
    f=32+((9*t)/5)
    print("temperatura = ", f, "Fº")


    
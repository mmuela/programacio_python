# RO_page025_diametrecilindre.py

hight = float(input("hight = "))
volume = float(input("volume = "))
pi = 3.1416

volume = volume / 1000
diameter = ((volume*4)/(pi*hight)) ** 0.5

print("diameter = ",diameter)
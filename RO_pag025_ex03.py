# RO_page025_ex03.py
# Dadas las tres dimensiones de un bloque rectangular calcule y muestre su área total y su volumen

hight = float(input("hight = "))
width = float(input("width = "))
depth = float(input("depth = "))

area =  (hight * width * 2) + (width * depth * 2) + (depth * hight * 2)
volume = (width * depth * hight)

print("volume = " ,volume, "m3")
print("area = " ,area, "m2")
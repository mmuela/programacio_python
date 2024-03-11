from math import*
def eq_2n_grau(a,b,c):
    dins_de_larrel=(b**2)-(4*a*c)
    if dins_de_larrel<0:
        print("error, l'arrel dona negativa",dins_de_larrel)
    else:
        x1=(-b+sqrt(dins_de_larrel))/(2*a)
        x2=(-b-sqrt(dins_de_larrel))/(2*a)
        print("1a solució = ",x1)
        print("2a solució = ",x2)
a=float(input("terme al amb x al quadrat = "))
b=float(input("terme amb x elevat a 1 = "))
c=float(input("terme independent = "))
eq_2n_grau(a,b,c)
# RO_page025_ex04.py
# La siguiente fórmula proporciona el enésimo término u de una progresión aritmética: u = a + (n − 1)r en donde a es el primer
# término,n es la cantidad de términos y r es la razón entre dos términos consecutivos. Calcular el valor de r dados u, a, n

u=float(input("u="))
a=float(input("a="))
n=float(input("n="))

r= (u-a)/(n-1)

print("r = ",r,)
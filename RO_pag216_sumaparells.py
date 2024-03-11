def sumarparells(llista):
    suma=0
    for i in llista:
        if i%2!=0:
            suma=suma+i
    return(suma)
llista=[]
n=int(input("nombre de nombres dins de la llista ="))
for j in range (0,n):
    p=int(input("nombre dins la llista :"))
    llista = llista + [p]
s=sumarparells(llista)
print(s)

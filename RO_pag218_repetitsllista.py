#RO_pag218_repetitsllista.py
v=[]
n=int(input("nombre de coses dins la llista v : "))
for i in range (0,n):
    a=float(input("nombre = "))
    v=v+[a]
u=[]
for e in v:
    if e not in u:
        u=u+[e]
print(v)
print(u)
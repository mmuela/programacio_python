#RO_pag083_ex04.py
x=int(input("num de 3 xifres"))
u=x%10
print(u)
d=x//10%10
print(d)
c=(x-(d*10+u))/100
print(c)
suma=c+(d*10)+(u*100)
print(suma)
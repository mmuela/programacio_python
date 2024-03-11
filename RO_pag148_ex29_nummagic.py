#RO_pag148_ex29_nummagic.py
dia=23
mes=1
anny=2024
suma=dia+mes+anny
m=suma//1000
d=suma%100//10
c=(suma%1000)//100
u=suma%10
n=m+d+c+u
while n>9:
    n1=n//10
    n2=n%10
    n=n1+n2
print("el teu nombre de la sort és: ",n)

#esamen1.py
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))

if (a>0) or (b>a) and (c!=d) :
    a=c
    b=0
else:
    c=c+d
    if c==0:
        c=c+b
    else:
        c=c-a
    b=a+c+d
print(a,b,c,d)
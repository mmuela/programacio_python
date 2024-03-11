#RO_page44_ex3.py

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
r=0
while (a>=b) and (c<=0):
    if (b+1) % 2 == 0:
        r=r+c
    b=b-1
    print(r)

print("r=",r)
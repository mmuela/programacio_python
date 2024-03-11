#RO_pag105_ulam.py
x=int(input("x ="))
i=1
while x>1:
    if x%2==0:
        x=x/2
    else:
        x=(3*x)+1
    print(x)
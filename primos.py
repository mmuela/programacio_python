def primos(n):
    a=0
    for i in range(2,n):
        if n%i==0:
            a=a+1
    if a>0:
        print("no es primer")
    elif a==0:
        print("el teu nombre es un primo")
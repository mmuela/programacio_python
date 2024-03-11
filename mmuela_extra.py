files=int(input("files = "))
a=1
for i in range (1,files+1):
    for columnes in range (0,i):
        print(a,end=" ")
        a=a+1
    print("")
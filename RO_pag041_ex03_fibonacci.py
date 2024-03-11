#RO_page41_ex03_fibonacci.py
import time
num=1
ant=0
n=int(input("nº de nombres de la serie ="))
x=0
for i in range(0,n+1):
    x=ant
    ant=num
    num=x+num
    time.sleep(0.5)
    if i == 1:
        print(1)
    print (i,".",num)
#nombres_primers
from math import*
n=int(input("n="))
i=2
while i>1 and i<n:
   if n%i==0:
        print("no primer")
   elif i==n:
        i=i+1
        print("primer")
        break
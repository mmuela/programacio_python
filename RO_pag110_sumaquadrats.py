#RO_pag110_sumaquadrats.py
n=int(input("n="))
s=0
for i in range (1,n+1):
    s=s+pow(i,2)
    i=i+1
print(s)
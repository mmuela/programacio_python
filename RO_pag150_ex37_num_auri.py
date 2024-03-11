#RO_pag150_ex37_num_auri.py
n=int(input('nº maxim fins al que ens diran parelles de nombres que fan el nombre auri ='))
a=1
b=1
for a in range(1, n+1):
    for b in range (1, n+1):
        x=a/b
        y=(a+b)/a
        if x==y:
            print(a,b)
            
            
#RO_page41_ex02.py
n=int(input("n="))
sis=0
nos=0

for i in range(1,n+1):
    print("vot ",i,"=")
    vot=int(input())
    if vot==1:
        sis=sis+1
    elif vot==0:
        nos=nos+1
nuls=n-(sis+nos)
print(sis,"sis", nos,"nos", nuls,"nuls")
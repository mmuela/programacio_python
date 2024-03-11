#RO_pag112_sumaimparells.py
n=int(input('inserti el nombre de xifres senars: '))
a=0
b=1
for i in range(n):
 a=a+b
 b=b+2
if a==n**2:
 print("és veraç")
else:
 print("es verídicn't")
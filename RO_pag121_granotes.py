#RO_pag121_granotes.py
from random import*
x=0
y=0
i=0
while not (4== abs(x) and 4==abs(y)):
    r=randint(1,4)
    if r==1:
        x=x+1
        i=i+1
    elif r==2:
        x=x-1
        i=i+1
    elif r==3:
        y=y+1
        i=i+1
    elif r==4:
        y=y-1
        i=i+1
    if x>4:
        x=x-1
    elif x<-4:
        x=x+1
    elif y>4:
        y=y-1
    elif y<-4:
        y=y+1
if 4==abs(x) and 4==abs(y):
    print(i)
    print("(",x,",",y,")")
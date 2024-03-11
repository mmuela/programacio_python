#RO_pag083_ex01.py
from math import*
dies=int(input("dies totals ="))
anys=dies//365
dies_restants=dies%365
mesos=dies_restants//30
dies_restants=dies_restants%30
print(anys,"anys")
print(mesos,"mesos")
print(dies_restants,"dies")
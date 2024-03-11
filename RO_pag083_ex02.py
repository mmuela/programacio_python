#RO_pag083_ex02.py

from math import*
dies=int(input("dies totals ="))
mesos=dies//30
dies_restants=dies%30
setmanes=dies_restants//7
dies_restants=dies_restants%7
print(mesos,"mesos")
print(setmanes,"setmanes")
print(dies_restants,"dies")
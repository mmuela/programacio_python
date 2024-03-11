#RO_pag083_ex05.py
from math import*
x=int(input("diners en dollars ="))

b100=x//100
b50=(x-(b100*100))//50
b20=(x-(b100*100)-(b50*50))//20
b10=(x-(b100*100)-(b50*50)-(b20*20))//10
b5=(x-(b100*100)-(b50*50)-(b20*20)-(b10*10))//5
b1=(x-(b100*100)-(b50*50)-(b20*20)-(b10*10)-(b5*5))//1
print(b100, "bitllets de 100 $")
print(b50, "bitllets de 50 $")
print(b20, "bitllets de 20 $")
print(b10, "bitllets de 10 $")
print(b5, "bitllets de 5 $")
print(b1, "bitllets de 1 $")
#RO_pg38_exemple
n = int(input("n ="))
s = 0
for i in range (1,n+1):
    k = 2 * i - 1
    s = s + k
    print(s,n,k,i)
if s==n**2:
    print("verdader")
else:
    print("fals")
print(s,n,k,i)

#RO_page41_ex01_for.py

np=10
ppm=0

for comptador in range (1,np+1):
    print ("pes del paquet",comptador,"en kg")
    pp=float(input())
    if pp>ppm:
        ppm=pp
print("el pes mes gran es val" ,ppm)
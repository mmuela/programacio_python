#RO_page41_ex01_while.py
np=1
ppm=0

while np!=10:
    print("pes del paquet",np,"en kg")
    pp=float(input())
    if pp>ppm:
        ppm=pp
    np=np+1
print("el pes del paquet mes fgran val:",ppm)
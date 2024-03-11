#RO_pag159_areasperimetrosyvolumenes.py
from math import*
import time
def quadrat():
    a=float(input("costat ="))
    A=a**2
    P=4*a
    print("area =",A)
    print("perimetre",P)
def triangle():
    a=float(input("costat 1 ="))
    b=float(input("costat 2 i base ="))
    c=float(input("costat 3="))
    h=float(input("alçada ="))
    A=b*h
    P=a+b+c
    print("area =",A)
    print("perimetre",P)
def rectangle():
    a=float(input("costat 1 ="))
    b=float(input('costat 2 ='))
    A=b*a
    P=2*b+2*a
    print("area =",A)
    print("perimetre",P)
def paralelogram():
    a=float(input('costat 1 ='))
    b=float(input('costat 2 i base ='))
    h=float(input('alçada ='))
    A=b*h
    P=2*(b+a)
    print("area =",A)
    print("perimetre",P)
def rombo():
    d=float(input('diagonal menor ='))
    D=float(input('diagonal major ='))
    a=float(input('costat ='))
    A=(d*D)/2
    P=4*a
    print("area =",A)
    print("perimetre",P)
def cometa(D,d,a,b):
    D=float(input('diagonal major ='))
    d=float(input('diagonal menor ='))
    a=float(input('costat 1 ='))
    b=float(input('costat 2 ='))
    A=(d*D)/2
    P=2*a+2*b
    print("area =",A)
    print("perimetre",P)
def trapecio():
    a=float(input('costat 1 ='))
    b=float(input('costat 2 i base petita='))
    c=float(input('costat 3 ='))
    B=float(input('costat 4 i base gran ='))
    h=float(input('alçada ='))
    A=((b+B)*h)/2
    p=a+b+c+B
    print("area =",A)
    print("perimetre",P)
def cercle():
    r=float(input('radi ='))
    A=pi*(r**2)
    P=2*pi*r
    print("area =",A)
    print("perimetre",P)
def altre_poligon_regular():
    n=int(input("nombre de costats ="))
    b=float(input("llargada d'un costat ="))
    a=float(input("apotema ="))
    P=n*b
    A=(P*a)/2
    print("area =",A)
    print("perimetre =",P)
def corona_circular():
    R=float(input("radi major ="))
    r=float(input("radi menor ="))
    A=pi((R**2)-(r**2))
    P=pi*2*R
    p=pi*2*r
    print("area =",A)
    print("perimetre interior =",p)
    print("perimetre exterior =",P)
def sector_circular():
    r=float(input("radi ="))
    n=float(input("angle (Cº) ="))
    A=(pi*(r**2)*n)/360
    P=2*r+(n*2*pi/360)
    print("area =",A)
    print("perimetre no se segur =",P)
def cub():
    a=float(input("costat ="))
    A=6*a*a
    V=a**3
    print("area =",A)
    print("volum =",V)
def cilindre():
    r=float(input("radi ="))
    h=float(input("alçada ="))
    A=2*pi*r*(h+r)
    V=pi*r*r*h
    print("area =",A)
    print("volum =",V)
def ortoedre():
    a=float(input("costat 1 ="))
    b=float(input("costat 2 ="))
    c=float(input("costat 3 ="))
    A=2*(a*b+a*c+b*c)
    V=a*b*c
    print("area =",A)
    print("volum =",V)
def prisme_recte():
    h=float(input("alçada ="))
    n=int(input("nombre de costats ="))
    a=float(input("apotema de la base ="))
    b=float(input("llargada costat ="))
    Pbase=n*b
    Abase=(P*a)/2
    A=Pbase*(h+a)
    V=Abase*h
    print("area =",A)
    print("volum =",V)
def con():
    R=float(input("radi base ="))
    h=float(input("alçada ="))
    g=sqrt((R**2)+(h**2))
    A=pi*R (R+g)
    V=pi*pow(R,2)*h/3
    print("area =",A)
    print("volum =",V)
def tronc_de_con():
    h=float(input("alçada ="))
    g=float(input("llargada d'el costat ="))
    R=float(input("radi major ="))
    r=float(input("radi menor ="))
    A=pi*[g*(r+R)+pow(r,2)+pow(R,2)]
    V=pi*h*(pow(R,2)+pow(r,2)+R*r)/3
    print("area =",A)
    print("volum =",V)
def esfera():
    R=float(input("radi ="))
    A = 4 * pi * (R**2)
    V = (4 * pi * (R**3))/3
    print("Area = ",A)
    print("Volum = ", V)
def piramide(P,a,a2,h,Ab):
    P
    A = (P * (a + a2))/2
    V = (Ab * h)/3
    print("Area = ",A)
    print("Volum = ", V)
def tetraedre_regular(a):#
    A = (a**2)* sqrt(3)
    V = ((a**3) * sqrt(2))/12
    print("Area = ",A)
    print("Volum = ", V)
def octaedre_regular(a):#
    A = (a**2)*2*sqrt(3)
    V = ((a**3) * sqrt(2))/3
    print("Area = ",A)
    print("Volum = ", V)
def tronc_de_piramide(p,P,a,ab,AB,h):#
    A=((p+P)/2)*a+ab+AB
    V=(ab+AB+sqrt(ab*AB))*h/3
    print("Area = ",A)
    print("Volum = ", V)
def casquet_esfèric(r,h):#
    A=2*pi*r*h
    V=pi*pow(h,2)*(3*r-h)/3
    print("Area = ",A)
    print("Volum = ", V)
def cunya_esfèrica(n,r):#
    A=(4*pi*r*r*n)/360
    V=(4*pi*(r**3)*n)/3*360
    print("area =",A)
    print("volum =",V)
def zona_segment_esfèric(R,h,r1,r2):
    A=2*pi*r*h
    V=(pi*h*((h**2)+(3*r1*r1)+(3*r2*r2)))/6
    print("area =",A)
    print("volum =",V)
sortida=False
while not sortida:
    print("")
    time.sleep(3)
    print("MENÚ:")
    time.sleep(0.2)
    print("1=quadrat")
    time.sleep(0.2)
    print("2=triangulo")
    time.sleep(0.2)
    print("3=rectangle")
    time.sleep(0.2)
    print("4=paralelogram")
    time.sleep(0.2)
    print("5=rombo")
    time.sleep(0.2)
    print("6=cometa")
    time.sleep(0.2)
    print("7=trapeci")
    time.sleep(0.2)
    print("8=cercle")
    time.sleep(0.2)
    print("9=altre poligon regular")
    time.sleep(0.2)
    print("10=corona circular")
    time.sleep(0.2)
    print("11=sector circular")
    time.sleep(0.2)
    print("12=cub")
    time.sleep(0.2)
    print("13=cilindre")
    time.sleep(0.2)
    print("14=ortoedre")
    time.sleep(0.2)
    print("15=prisme recte")
    time.sleep(0.2)
    print("16=con")
    time.sleep(0.2)
    print("17=tronc de con")
    time.sleep(0.2)
    print("18=esfera")
    time.sleep(0.2)
    print("19=piramide")
    time.sleep(0.2)
    print("20=tetraedre regular")
    time.sleep(0.2)
    print("21=octaedre regular")
    time.sleep(0.2)
    print("22=tronc de piramide")
    time.sleep(0.2)
    print("23=casquet esfèric")
    time.sleep(0.2)
    print("24=cunya esfèrica")
    time.sleep(0.2)
    print("25=zona segment esfèric")
    time.sleep(0.2)
    print("26=sortir")
    time.sleep(0.2)
    x=int(input("tri la seva forma: "))
    if x==1:
        quadrat()
    elif x==2:
        triangle()
    elif x==3:
        rectangle()
    elif x==4:
        paralelogram()
    elif x==5:
        rombo()
    elif x==6:
    elif x==7:
    elif x==8:
    elif x==9:
    elif x==10:
    elif x==11:
    elif x==12:
    elif x==13:
    elif x==14:
        
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==5
    elif x==26:
        sortida=True

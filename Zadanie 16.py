from math import sqrt

def MAKS(a,b):
    if a>b :
        print(f"Liczba {a} jest wieksza")
    elif a<b :
        print (f"Liczba {b} jest wieksza")
    else:
        print ("liczby są równe")

def MIN(a,b,c):
    if a<c and a<b :
        return a 
    elif b<c and b<a :
        return b
    else :
        return c

def czyParzysta(a) :
    if a%2==0 :
        return (f"Liczba {a} jest parzysta")
    else :
        return (f"Liczba {a} jest nieparzysta")

def BezWzgl(a) :
    a=a*a 
    a=sqrt(a)
    return a



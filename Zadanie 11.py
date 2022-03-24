x=int(input("Podaj współrzędną x  w układzie współrzędnych"))
y=int(input("Podaj współrzędną y  w układzie współrzędnych"))
if x>0 and y>0 :
    print(f"Punkt {x, y} znajduje się w I ćwiartce układu współrzędnych")
elif x<0 and y>0 :
    print(f"Punkt {x, y} znajduje się w II ćwiartce układu współrzędnych")
elif x<0 and y<0 :
    print(f"Punkt {x, y} znajduje się w III ćwiartce układu współrzędnych")
elif x>0 and y<0 :
    print(f"Punkt {x, y} znajduje się w IV ćwiartce układu współrzędnych")
elif x==0 and y != 0 :
    print(f"Punkt {x, y} znajduje się na osi y")
elif x!=0 and y == 0 :
    print(f"Punkt {x, y} znajduje się na osi x")
elif x==0 and y == 0 :
    print(f"Punkt {x, y} znajduje się na w centrum układu współrzędnych")
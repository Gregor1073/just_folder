from math import sqrt
choice=int(input("Wybierz 1 aby skorzystać z kalkulatora\nWybierz 2 aby skorzystać z kalkulatora obiętości\nWybierz 3 Aby uzyskać informacje o liczbie"))
while choice!=1 and choice!=2 and choice!= 3:
    print("dokonaj wyboru jeszcze raz")
    choice=int(input("Wybierz 1 aby skorzystać z kalkulatora\nWybierz 2 aby skorzystać z kalkulatora obiętości\nWybierz 3 Aby uzyskać informacje o liczbie"))
if choice==1:
    znak=int(input("Jakie działanie chcesz wykonać? \n 1)Dodawanie (wpisz 1) \n 2)Odejmowanie (wpisz 2) \n 3)Mnozenie (wpisz 3) \n 4)Dzielenie (wpisz 4)\n 5)Potęgowanie (wpisz 5)"))
    while znak!=1 and znak!=2 and znak!=3 and znak!=4 and znak!=5:
        print("dokonaj wyboru jeszcze raz")
        znak=int(input("Jakie działanie chcesz wykonać? \n 1)Dodawanie (wpisz 1) \n 2)Odejmowanie (wpisz 2) \n 3)Mnozenie (wpisz 3) \n 4)Dzielenie (wpisz 4)\n 5)Potęgowanie (wpisz 5)"))
    if znak==1 :
        liczba_a=int(input("podaj liczbe a"))
        liczba_b=int(input("podaj liczbe b"))
        print("wynik=", liczba_a+liczba_b)
    elif znak==2 :
        liczba_a=int(input("podaj liczbe a"))
        liczba_b=int(input("podaj liczbe b"))
        print("wynik=", liczba_a-liczba_b)
    elif znak==3 :
        liczba_a=int(input("podaj liczbe a"))
        liczba_b=int(input("podaj liczbe b"))
        print("wynik=", liczba_a*liczba_b)
    elif znak==4 :
        liczba_a=int(input("podaj liczbe a"))
        liczba_b=int(input("podaj liczbe b"))
        if liczba_b==0 :
            print("Nie dziel przez 0")
            liczba_b=int(input("podaj liczbe b"))
            print("wynik=", liczba_a/liczba_b)
        else :
            print("wynik=", liczba_a/liczba_b)
    elif znak==5:
        liczba_a=int(input("Podaj podstawę potęgi"))
        liczba_b=int(input("podaj wykładnik potęgi"))
        print("wynik =", liczba_a**liczba_b)
elif choice==2:
    znak=int(input("Jakiej bryły obiętość chcesz policzyć? \n 1)Sześcian (wpisz 1) \n 2)Prostopadłościan (wpisz 2) \n 3)Ostrosłup (wpisz 3) \n"))
    while znak!=1 and znak!=2 and znak!=3 and znak!=4 and znak!=5:
        print("dokonaj wyboru jeszcze raz")
        znak=int(input("Jakiej bryły obiętość chcesz policzyć? \n 1)Sześcian (wpisz 1) \n 2)Prostopadłościan (wpisz 2) \n 3)Ostrosłup (wpisz 3) \n"))
    if znak==1:
        a=int(input("Podaj długość krawędzi sześcianu"))
        print(f"Objętość sześcianu wynosi {a**3}")
    elif znak==2:
        a=int(input("Podaj długość pierwszej krawędzi prostopadłościanu"))
        b=int(input("Podaj długość drugiej krawędzi prostopadłościanu"))
        c=int(input("Podaj długość trzeciej krawędzi prostopadłościanu"))
        print(f"Objętość prostopadłościanu wynosi {a*b*c}")
    elif znak==3:
        a=int(input("Podaj długość pierwszej krawędzi podstawy ostrosłupa"))
        b=int(input("Podaj długość drugiej krawędzi podstawy ostrosłupa"))
        h=int(input("Podaj długość wysokości ostrosłupa"))
        print(f"Objętość ostrosłupa wynosi {a*b*h*1/3}")
elif choice==3:
    a=int(input("podaj liczbę"))
    def CzyDodatnia(a):
        if a>0:
            print("Liczba jest dodatnia")
        elif a<0:
            print("Liczba jest ujemna")
    def CzyPodzielna(a):
        if a%3==0:
            print("Twoja liczba jest podzielna przez 3")
        elif a%3!=0:
            print("Twoja liczba nie jest podzielna przez 3")
    def BezWzgl(a) :
        a=a*a 
        a=sqrt(a)
        return a
    print(
    CzyDodatnia(a),
    CzyPodzielna(a),
    BezWzgl(a)
    )
    






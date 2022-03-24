znak=int(input("Jakie działanie chcesz wykonać? \n 1)Dodawanie (wpisz 1) \n 2)Odejmowanie (wpisz 2) \n 3)Mnozenie (wpisz 3) \n 4)Dzielenie (wpisz 4)\n"))
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
    else :
        print("wynik=", liczba_a/liczba_b)
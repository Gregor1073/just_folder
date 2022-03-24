import random
for i in range(1) :
    los=random.randint(1, 20)
liczba=int(input("odgadnij wylosowaną liczbę"))
proby=[]
proby.append(liczba)

if los==liczba and len(proby)==1 :
    print(f"Gartulacje, udało ci się odgadnąć liczbe za {len(proby)} razem")
else:
    while liczba!=los:
        proby.append(liczba)
        liczba=int(input("Spróbuj jeszcze raz. Jaką liczbę wylosował komputer"))
        if liczba==los:
            print(f"Brawo. Do odgadnięcia liczby potrzebowałeś {len(proby)} prób")
    
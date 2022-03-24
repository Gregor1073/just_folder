import random
losowanie=[]
strzaly=[]
for i in range(6) :
    a=random.randint(1,50)
    losowanie.append(a)
    b=int(input(f"Podaj liczbę {i+1} z 6 "))
    while b<1 or b>50:
        print("Podaj liczbę z zakresu od 1 do 50")
        b=int(input(f"Podaj liczbę {i+1} z 6 "))
    strzaly.append(b)
print(f"wylosowane liczby {losowanie}")
print(f"podane przez ciebie liczby {strzaly}")

traf=set(losowanie)&set(strzaly)

if len(traf)>0 :
    print(f"Odgadłeś {len(traf)} liczb. Oto one {traf}")
else :
    print("nie odgadłeś zadnej liczby")


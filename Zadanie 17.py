import random
import string

slowa=["samochód","komputer","informatyka","klawiatura","kontynent","wszechświat","program","słuchawki","piosenkarz","gitara","pianino","szkoła","monitor","termos","wisielec","motocykl","oprogramowanie","mieszkanie","telefon","gaśnica"]
pole=[]
live=[]
traf=[]
wylosowane=(random.choice(slowa))
len(wylosowane)
lliter=len(wylosowane)
for i in range(lliter):
    pole.append("_")
print("\n", *pole)


while len(live)<5:   
    strzal=input("\nPodaj literę którą chcesz strzelić ")
    if strzal in wylosowane : 
        for i in range(lliter) :
            if wylosowane[i] == strzal:
                pole[i]=strzal 
                traf.append(1)
        print(*pole)   
    else :
        print("nietrafiłeś")
        live.append(1)
        print(*pole)

    if "_" not in pole:
        print("Odgadłeś całe słowo!!! Gratulacje")
        exit()

print(f"Niestety skończyły ci się zycia. Twoje słowo to {wylosowane} ")

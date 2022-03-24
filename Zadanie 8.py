import random
print("Podaj zakres losowania liczb")
liczba_a=int(input("Od:"))
liczba_b=int(input("Do:"))
for i in range(6) :
    print(random.randint(liczba_a, liczba_b))
wzrost=float(input("Podaj swój wzrost (w metrach)"))
waga=float(input("Podaj swoją masę (w kilogramach)"))
BMI=waga/wzrost**2
if BMI<20 :
    print(f"Twoje BMI wynosi {BMI} ---> Niedowaga")
elif BMI >=20 and BMI < 25 :
    print(f"Twoje BMI wynosi {BMI} ---> Waga prawidłowa")
elif BMI>=25 and BMI<30 :
    print(f"Twoje BMI wynosi {BMI} ---> Nadwaga")
else:
    print(f"Twoje BMI wynosi {BMI} ---> Otyłość")
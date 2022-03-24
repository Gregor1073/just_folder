import random
prog=[]
uzyt=[]
while len(prog)<3 or len(uzyt)<3 :
    knp=int(input("Aby wybrać kamień wpisz 1 \nAby wybrać papier wpisz 2 \nAby wybrać nozyce wpisz 3\n"))
    while knp!=1 and knp!=2 and knp!=3 :
        knp=int(input("Twojego wyboru nie ma w menu opcji \nAby wybrać kamień wpisz 1 \nAby wybrać papier wpisz 2 \nAby wybrać nozyce wpisz 3\n"))

    for i in range(1) :
        los=random.randint(1,3)
    if los==knp and knp==1 :
        print("Remis! Program tez wybrał kamień spróbuj ponownie")
    elif los==knp and knp==2 :
        print("Remis! Program tez wybrał papier ponownie")
    elif los==knp and knp==3 :
        print("Remis! Program tez wybrał nozyce spróbuj ponownie")
    elif los==1 and knp==2 :
        print("Zdobywasz punkt! Program wybrał kamień")
        uzyt.append(1)
    elif los==1 and knp==3 :
        print("Program zdobywa punkt, poniewaz wybrał kamień!")
        prog.append(1)
    elif los==2 and knp==3 :
        print("Zdobywasz punkt! Program wybrał papier")
        uzyt.append(1)
    elif los==2 and knp==1 :
        print("Program zdobywa punkt, poniewaz wybrał papier")
        prog.append(1)
    elif los==3 and knp==1 :
        print("Zdobywasz punkt! Program wybrał nozyce")
        uzyt.append(1)
    elif los==3 and knp==2 :
        print("Program zdobywa punkt, poniewaz wybrał nozyce")
        prog.append(1)
if len(prog)==3:
    print("program wygrał")
elif len(uzyt)==3:
    print("wygrałeś!")


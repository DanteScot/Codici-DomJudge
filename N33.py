import random
from random import randint

pl=0
pc=0
giocoPL=-1
giocoPC=-1
random.seed(0)
while True:
    while True:
        giocoPL=int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
        if giocoPL==1 or giocoPL==2 or giocoPL==3:
            break
    
    if giocoPL==1:
        print("hai giocato sasso")
    elif giocoPL==2:
        print("hai giocato carta")
    elif giocoPL==3:
        print("hai giocato forbice")


    giocoPC=randint(1,3)
    if giocoPC==1:
        print("il PC ha giocato sasso")
    elif giocoPC==2:
        print("il PC ha giocato carta")
    elif giocoPC==3:
        print("il PC ha giocato forbice")

    if giocoPL==giocoPC:
        print("Pari:")
    elif (giocoPL==1 and giocoPC==3) or (giocoPL==2 and giocoPC==1) or (giocoPL==3 and giocoPC==2):
        print("Vinci tu:")
        pl+=1
    else:
        print("Vince il PC:")
        pc+=1

    print(pl,"-",pc,sep="")

    if pl==3:
        print("Hai vinto la sfida!")
        break
    elif pc==3:
        print("Il PC ha vinto la sfida!")
        break
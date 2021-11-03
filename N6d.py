mese=int(input())

if 1<=mese<=12:
    if mese%3==0:
        giorno=int(input())
        if giorno>=1 and giorno<=20:
            mese-=1
        else:
            mese+=1

    if mese==13:
        mese=1

    if mese==1 or mese==2:
        print("INVERNO", end="")
    if mese==4 or mese==5:
        print("PRIMAVERA", end="")
    if mese==7 or mese==8:
        print("ESTATE", end="")
    if mese==10 or mese==11:
        print("AUTUNNO", end="")

else:
    print("MESE NON VALIDO", end="")
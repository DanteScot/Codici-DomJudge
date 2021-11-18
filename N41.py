posti=[0,0,0,0,0,0,0,0,0,0]
cambia=False

def si():
    global posti
    global cambia

    trovato=False
    for i in range(5):
        if posti[i]==0:
            trovato=True
            posti[i]=1
            print("Reparto fumatori, posto", i+1)
            break

    if trovato==False:
        cambia=True

def no():
    global posti
    global cambia
    trovato=False
    for i in range(5,10):
        if posti[i]==0:
            trovato=True
            posti[i]=1
            print("Reparto NON fumatori, posto", i+1)
            break

    if trovato==False:
        cambia=True




while 0 in posti:
    scelta=int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    cambia=False

    if scelta==1:
        si()
    else:
        no()


    if cambia==True:
        temp=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
        if temp=="N" or temp=="n":
            print("Il prossimo volo parte tra 3 ore")
        else:
            if scelta==1:
                no()
            else:
                si()

def Pari(lista):
    cresc=True
    for i in range(len(lista)):
        if i!=0:
            if lista[i]<=lista[i-1]:
                cresc=False
    
    return cresc

def Dispari(lista):
    disp=True
    for x in lista:
        if x%2==0:
            disp=False

    return disp

def Main():
    out="SI"
    x=int(input())
    pari=[]
    dispari=[]

    for i in range(x):
        if i%2==0:
            pari.append(int(input()))
        else:
            dispari.append(int(input()))

    p=Pari(pari)
    d=Dispari(dispari)

    if p==False or d==False:
        out="NO"

    print(out,end="")

Main()
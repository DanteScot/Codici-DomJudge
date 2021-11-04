seq=0
vocali="aeiou"
x=input()
if x!=".":
    trovato=False
    for i in range(len(vocali)):
        if x==vocali[i]:
            trovato=True
    
    nec=not trovato

    seq+=1

    while True:
        x=input()
        if x==".":
            break

        trovato=False
        for i in range(len(vocali)):
            if x==vocali[i]:
                trovato=True

        if trovato==nec:
            nec=not nec
        else:
            seq+=1

print(seq,end="")
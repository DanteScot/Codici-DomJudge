out="NESSUNA VOCALE"
vocali="aeiou"
while True:
    x=input()
    if x==".":
        break
    
    trovato=False
    for i in range(len(vocali)):
        if x==vocali[i]:
            trovato=True
        
    if trovato==True:
        out="ALMENO 1 VOCALE"

print(out,end="")
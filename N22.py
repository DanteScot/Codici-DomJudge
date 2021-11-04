out="NO"
alfabeto="qwertyuiopasdfghjklzxcvbnm"
ALFABETO="QWERTYUIOPASDFGHJKLZXCVBNM"
while True:
    x=input()
    if x==".":
        break
    
    trovato=False
    for i in range(len(alfabeto)):
        if x==alfabeto[i]  or x==ALFABETO[i]:
            trovato=True
        
    if trovato==True:
        out="SI"

print(out,end="")
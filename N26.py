x=-1
y=""
alfabeto="qwertyuiopasdfghjklzxcvbnm"
ALFABETO="QWERTYUIOPASDFGHJKLZXCVBNM"
out="NO"
while True:
    n=input()
    if n=="*":
        break

    if x==1 and n in ALFABETO:
        out="SI"
    elif x!=1 and n in ALFABETO:
        x=1
    elif x==0 and n in alfabeto:
        if n==y:
            out="SI"
        else:
            y=n
            x=0
    elif x!=0 and n in alfabeto:
        x=0
        y=n
    else:
        y=""
        x=-1

print(out,end="")
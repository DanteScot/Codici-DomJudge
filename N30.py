abc="qwertyuiopasdfghjklzxcvbnm"
ABC="QWERTYUIOPASDFGHJKLZXCVBNM"
prec=""
out="NO"

while True:
    x=input()
    if x=="*":
        break

    if x in abc or x in ABC:
        if x==prec:
            out="SI"
        else:
            prec=x

print(out,end="")
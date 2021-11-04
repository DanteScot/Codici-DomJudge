x=input()
out="NO"
if x=="*":
    out="NO"
else:
    while x!="*":
        prec=x
        x=input()
        if prec==x:
            out="SI"

print(out,end="")
out="NO"
prec=-1
while True:
    x=int(input())
    if(x==0):
        break

    if (x%2==0 and prec%2==0):
        out="SI"
    
    if prec!=-1:
        if (x+prec)%x==0 or (x+prec)%prec==0:
            out="SI"
    
    prec=x

print(out,end="")
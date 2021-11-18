asc=False
desc=False
prec=None
eseguito=False
temp=0
out="SI"

while True:
    x=int(input())
    if x==0:
        break
    temp+=1
    if temp>1:
        if x>prec and asc==False:
            asc=True
        elif x<prec and asc==True and eseguito==False:
            desc=True
            eseguito=True

        if x>prec and desc==True or x==prec:
            out="NO"

    prec=x

if temp<2 or desc==False:
    out="NO"
print(out,end="")
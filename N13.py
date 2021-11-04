a=int(input())
b=int(input())
aMax=round(a/2)
bMax=round(b/2)
primi=True
i=2

while i<=aMax:
    if a%i==0:
        primi=False
    i+=1

if primi:
    i=2
    while i<=bMax:
        if b%i==0:
            primi=False
        i+=1

if primi!=True:
    print("non entrambi primi",end="")
else:
    if abs(a-b)!=2:
        print("non gemelli",end="")
    else:
        print("gemelli",end="")
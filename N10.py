a=input()
aInv=""

aLen=len(a)-1

while aLen>=0:
    aInv+=a[aLen]
    aLen-=1

print(int(a)-int(aInv),end="")
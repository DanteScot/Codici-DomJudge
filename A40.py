val=[]
div=0
som=0

while True:
    x=int(input())
    if x==-50:
        break

    div+=1
    som+=x
    val.append(x)

if div!=0:
    med=som//div
    min=100000
    for i in range(len(val)):
        if med<=val[i]<min:
            min=val[i]

if len(val)==0:
    min="VUOTA"
print(min,end="")
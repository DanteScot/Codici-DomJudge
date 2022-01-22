lista=""
div=0
som=0
for i in range(100):
    temp=int(input())
    if temp<-50 or temp>50:
        lista+=str(temp)
    else:
        div+=1
        som+=temp

if lista=="":
    print("VUOTO1")
else:
    print(lista)

if div==0:
    print("VUOTO2",end="")
else:
    tot=som/div
    temp=round(tot,6)
    print(temp,end="")
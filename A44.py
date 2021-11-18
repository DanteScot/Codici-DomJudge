n=input()
x=[]
y=[]

for i in range(round(len(n)/2)):
    x.append(n[i])
for i in range(round(len(n)/2),len(n)):
    y.append(n[i])

somX=0
somY=0

for i in range(len(x)):
    somX+=int(x[i])
for i in range(len(y)):
    somY+=int(y[i])

if somX==somY:
    print("FORTUNATO",end="")
else:
    print("SFORTUNATO",end="")
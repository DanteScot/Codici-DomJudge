x=[]
out="SI"

while True:
    temp=int(input())
    if temp==0:
        break

    x.append(temp)

for i in range(len(x)):
    for j in range(x[i]):
        if 2**j==x[i]:
            break

        if 2**j>x[i]:
            out="NO"
            break

print(out,end="")
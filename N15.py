out=0
serie=""
n=0
while out!=3:
    x=int(input())
    if x==9:
        out+=1
    else:
        out=0
    
    serie+=str(x)

for i in range(len(serie)-3):
    if serie[i]==serie[i+1]==serie[i+2]:
        n+=1

print(n,end="")

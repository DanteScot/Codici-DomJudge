x=int(input())
out="SI"
max=round(x/2)
i=2

while i<=max:
    if x%i==0:
        out="NO"
    i+=1

print(out,end="")
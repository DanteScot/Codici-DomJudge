x=int(input())
y=int(input())
tot=0

i=x

while i<=y:
    if i%2!=0:
        tot+=i

    i+=1

print(tot,end="")
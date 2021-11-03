x=1
temp=0

while x!=0:
    x=int(input())
    if x%2!=0 and x%3==0:
        temp+=1

print(temp,end="")
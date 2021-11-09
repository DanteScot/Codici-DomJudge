x=int(input())
out="NO"
count=0
while True:
    n=int(input())
    if n==-1:
        break

    if n==0:
        count+=1
    else:
        count=0

    if count==x:
        out="OK"

print(out,end="")
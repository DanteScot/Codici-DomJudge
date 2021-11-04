n=int(input())
x=""
while True:
    temp=input()
    if int(temp)==-1:
        break

    x+=temp

out="NO"

if len(x)<n:
    out="NO"
else:
    for i in range(len(x)-n+1):
        temp=i
        max=temp+n
        trovato=False
        while temp<max:
            if int(x[temp])>n:
                trovato=True
            temp+=1
        
        if trovato==False:
            out="OK"

print(out,end="")

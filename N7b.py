x=int(input())
n=int(input())

i=0
output=""
while i<n:
    i+=1
    temp=input()
    if int(temp)<x and int(temp)%2==0:
        output+=temp

if output!="":
    print(output, end="")
x=[]
out="OK"

for i in range(10):
    x.append(int(input()))

n=int(input())

for i in range(len(x)):
    if x[i]%n==0:
        out="NO"

print(out,end="")
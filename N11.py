x=input()
len=len(x)-1
i=0
out="SI"

while i<=len:
    if int(x[i])==0:
        out="NO"
    i+=1

print(out,end="")
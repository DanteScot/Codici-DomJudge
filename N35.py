out=0
while True:
    x=int(input())
    if x==0:
        break

    n=input()

    if n=="s":
        out+=x
    elif n=="m":
        out+=x*60
    elif n=="h":
        out+=x*3600

print(out,end="")
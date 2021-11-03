n=int(input())
temp=False
while n!=5:
    if n%5==0:
        temp=True

    n=int(input())

if temp:
    print("ALMENO 1", end="")
else:
    print("NESSUNO", end="")
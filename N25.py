continua=True
somma=0
temp=False
while continua:
    x=int(input())
    
    if x==0 and temp==True:
        break
    else:
        temp=False

    
    somma+=x
    if x==0:
        print(somma)
        somma=0
        temp=True
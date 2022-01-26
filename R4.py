def R(lista,x,n):
    if x==0:
        return 0
    
    tot=0
    for i in range(n):
        if lista[i]==x:
            tot+=1
            lista[i]=0
    
    tot+=R(lista,tot,n)
    return tot


def Main():    
    x=int(input())
    n=int(input())
    lista=[]
    for i in range(n):
        lista.append(int(input()))

    print(R(lista,x,n),end="")

Main()
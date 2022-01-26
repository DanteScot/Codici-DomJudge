n=int(input())
out="NO"
lista=[]
for i in range(n):
    lista.append(int(input()))

if n%2==0:
    temp=round(len(lista)/2)
    lista1=lista[:temp]
    lista2=lista[temp:]

    if lista1==lista2:
        out="SI"

print(out,end="")
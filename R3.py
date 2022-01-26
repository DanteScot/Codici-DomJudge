def Normale(matrice,n):
    tot=0
    for i in range(n,-1,-1):
        ind=n-i
        tot+=matrice[ind][i]
    
    return tot

def Ricorsiva(matrice,y,x):
    if x<0:
        return 0
    else:
        tot=0
        tot+=matrice[y][x]+Ricorsiva(matrice,y+1,x-1)
        return tot

def Main():
    matrice=[]
    n=int(input())
    for i in range(n):
        matrice.append([0]*n)

    for i in range(n):
        for j in range(n):
            matrice[i][j]=int(input())

    tot1=Normale(matrice,n-1)
    tot2=Ricorsiva(matrice,0,n-1)
    print(tot1,";",tot2,end="",sep="")

Main()
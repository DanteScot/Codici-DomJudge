matrice=[]
for i in range(10):
    matrice.append([0]*10)

x=int(input())
n=1
tot=0

for i in range(10):
    for j in range(10):
        if n<=x:
            matrice[i][j]=n
            n+=1
        else:
            n=1
            matrice[i][j]=n
            n+=1

for i in range(9,-1,-1):
    ind=9-i
    tot+=matrice[ind][i]

print(tot,end="")
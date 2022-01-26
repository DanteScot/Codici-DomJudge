n=int(input())
matrice=[]
for i in range(n):
    matrice.append([0]*n)

for i in range(n):
    for j in range(n):
        matrice[i][j]=int(input())

croce=n//2
totCroce=0

#linea verticale
for i in range(n):
    totCroce+=matrice[i][croce]

#linea orizzontale
for i in range(n):
    totCroce+=matrice[croce][i]

totCroce-=matrice[croce][croce]
totAll=0

#somma totale
for i in range(n):
    for j in range(n):
        totAll+=matrice[i][j]

totAll-=totCroce

if totCroce>totAll:
    print("OK",end="")
else:
    print("NO",end="")
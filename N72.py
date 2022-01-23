cor=input()
studenti=[]
voti=[]
for i in range(90):
    pt=0
    mat=input()
    risp=input()
    for x in range(20):
        if risp[x]!="X":
            if risp[x]==cor[x]:
                pt+=2
            else:
                pt-=1

    studenti.append(mat)
    voti.append(pt)

for i in range(90):
    print(studenti[i],voti[i])
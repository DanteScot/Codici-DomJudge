def visualizzaPavimento(pavimento, dim):
    for i in range(dim):
        for j in range(dim):
            if pavimento[i][j]==1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def istruzioni(x):
    while True:
        temp=input()
        try:
            x=int(temp)
            if x==9:
                break

            if x in range(1,8):
                com.append(x)
        except:
            x=temp

def moveN(pos,passi):
    global tavola
    global writing
    if pos[0]-1-passi<0:
        passi=0+pos[0]
    if passi<1:
        return
    temp=pos[0]-1
    if writing==True:
        for i in range(temp,temp-passi,-1):
            tavola[i][pos[1]]=1
    pos[0]-=passi

def moveS(pos,passi):
    global tavola
    global writing
    if pos[0]+1+passi>19:
        passi=19-pos[0]
    if passi<1:
        return
    temp=pos[0]+1
    if writing==True:
        for i in range(temp,temp+passi):
            tavola[i][pos[1]]=1
    pos[0]+=passi

def moveE(pos,passi):
    global tavola
    global writing
    if pos[1]+1+passi>19:
        passi=19-pos[1]
    if passi<1:
        return
    temp=pos[1]+1
    if writing==True:
        for i in range(temp,temp+passi):
            tavola[pos[0]][i]=1
    pos[1]+=passi

def moveO(pos,passi):
    global tavola
    global writing
    if pos[1]-1-passi<0:
        passi=0+pos[1]
    if passi<1:
        return
    temp=pos[1]-1
    if writing==True:
        for i in range(temp,temp-passi,-1):
            tavola[pos[0]][i]=1
    pos[1]-=passi

def move(x,pos):
    passi=int(input("passi?"))
    print()

    if x==3:
        moveE(pos,passi)
    elif x==4:
        moveO(pos,passi)
    elif x==5:
        moveS(pos,passi)
    elif x==6:
        moveN(pos,passi)

            

    


writing=True
pos=[0,0]

tavola=[]
for i in range(20):
    tavola.append([0]*20)

com=[]
istruzioni(com)

for i in range(len(com)):
    if com[i]==1:
        writing=False
    elif com[i]==2:
        writing=True
    elif com[i] in range(3,7):
        move(com[i],pos)
    else:
        visualizzaPavimento(tavola,20)
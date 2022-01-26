lista=[]
while True:
    temp=input()
    lista.append(temp)
    if temp==":":
        break

controllo=True
if lista[0]!="def":
    controllo=False

if controllo:
    if not lista[1].isidentifier():
        controllo=False

if controllo:
    if lista[2]!="(":
        controllo=False

if controllo:
    if lista[len(lista)-2]!=")":
        controllo=False

nuovaLista=lista[3:len(lista)-2]
nec=False
for x in nuovaLista:
    if nec==True and x==",":
        nec=False
        continue
    elif nec==True and x!=",":
        controllo=False
        break
    elif nec==False and x==",":
        controllo=False
        break 
    elif nec==False and x!=",":
        nec=True
        if not x.isidentifier():
            controllo=False
            break 

if controllo:
    print("SI",end="")
else:
    print("NO",end="")
def corretto(frase, indice):
    global out2

    for i in range(indice, len(frase)):
        if frase[i]==")":
            if i-indice==1:
                out2="no2"
                return
            else:
                return

def elimina(frase, indice):
    global out1
    
    for i in range(indice, len(frase)):
        if frase[i]==")":
            frase.pop(i)
            frase.pop(indice)
            return frase
    
    out1="no1"
    return frase


out1="ok1"
out2="ok2"
temp=input()
frase=[]
for x in temp:
    frase.append(x)

for i in range(len(temp)):
    if temp[i]=="(":
        corretto(frase, i)

for x in temp:
    if x=="(":
        frase=elimina(frase, frase.index("("))

if out1=="ok1":
    if frase.count(")")!=0:
        out1="no1"

print(out1)
print(out2)
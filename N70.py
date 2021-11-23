vocali="aeiou"

parola=input()
x=list(parola)
parola=""

for i in range(len(x)):
    if x[i] in vocali:
        parola+=x[i]
        parola+="f"
        parola+=x[i]
    else:
        parola+=x[i]

out=""
for i in range(len(parola)//2,len(parola)):
    out+=parola[i]

for i in range(len(parola)//2):
    out+=parola[i]

print(out,end="")
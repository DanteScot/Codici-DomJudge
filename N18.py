str=""
while True:
    x=input()
    str+=x

    if x=="k" and str[len(str)-2]=="o":
        break

print(len(str)-2,end="")

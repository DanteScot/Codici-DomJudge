n=int(input())

prezzo=5

if n>80 and n<=140:
    n-=80
    prezzo+=n*0.10
elif n>140 and n<=190:
    prezzo+=6
    n-=140
    prezzo+=n*0.07
elif n>190:
    prezzo+=9.5
    n-=190
    prezzo+=n*0.05

print(round(prezzo,3),end="")
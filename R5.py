def R(x,i):
    out=""
    if i!=len(x):
        out+=R(x,i+1)
        out+=x[i]
    return out

def Main():
    n=int(input())
    x=""
    for i in range(n):
        x+=input()
    print(R(x,0),end="")

Main()
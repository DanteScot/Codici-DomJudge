def R(x):
    if x==0:
        return 2
    else:
        return 3*(x+1)*R(x-1)

def Main():
    x=int(input())
    print(R(x),end="")

Main()
def R(a,b):
    if a%b==0:
        return b
    else:
        temp=a%b
        a=b
        b=temp
        return R(a,b)

def Main():
    a=int(input())
    b=int(input())
    print(R(a,b),end="")

Main()
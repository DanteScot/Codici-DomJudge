a=int(input())
b=int(input())
c=int(input())

valido=a<b+c and b<a+c and c<a+b

if valido:
    if a==b==c:
        print("TRIANGOLO EQUILATERO",end="")
    elif a==b or b==c:
        print("TRIANGOLO ISOSCELE",end="")
    else:
        print("TRIANGOLO SCALENO",end="")
else:
    print("NO",end="")
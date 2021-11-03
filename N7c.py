n=int(input())
x=0
y=0
z=0

while n!=0:
    if n==1:
        x+=1
    elif n==2:
        y+=1
    elif n==3:
        z+=1
    
    n=int(input())


if x==0 and y==0 and z==0:
    print("BALLOTTAGGIO",end="")
else:
    tot=x+y+z
    xPer=round(x/tot*100,1)
    yPer=round(y/tot*100,1)
    zPer=round(z/tot*100,1)
    print("1",x,xPer)
    print("2",y,yPer)
    print("3",z,zPer)

    if xPer>50:
        print("VINCE 1",end="")
    elif yPer>50:
        print("VINCE 2",end="")
    elif zPer>50:
        print("VINCE 3",end="")
    else:
        print("BALLOTTAGGIO",end="")
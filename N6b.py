x=float(input())
y=float(input())

if y==0:
    print(round(x,3),end="")
elif y==1:
    print(round(x-((x*10)/100),3),end="")
elif y==2:
    print(round(x-((x*15)/100),3),end="")
elif y==3:
    print(round(x-((x*25)/100),3),end="")
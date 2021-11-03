n=int(input())

bis=True

if n%4!=0:
    bis=False
else:
    if n%100==0:
        if n%400!=0:
            bis=False

if bis==True:
    print("BISESTILE",end="")
else:
    print("NON BISESTILE",end="")
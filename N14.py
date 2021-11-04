n=int(input())
out=""
err=False

if(n==-1):
    print("VUOTO",end="")
else:
    while n!=-1:
        if n<0 or n>9:
            err=True
        else:
            out+=str(n)
        
        n=int(input())

    if err:
        print("ERRORE",end="")
    else:
        print(out)
        if int(out)%3==0:
            print("SI",end="")
        else:
            print("NO",end="")
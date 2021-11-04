out="NESSUNA"
while True:
    x=input()
    if x=="*":
        break
    
    try:
        temp=int(x)
        out="ALMENO UNA"
    except:
        temp=0

print(out,end="")
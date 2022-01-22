vocali="aeiou"
out="OK"
x=None
for i in range(100):
    temp=input()
    if x==None and temp in vocali:
        x=temp
    if temp in vocali and temp!=x:
        out="ERRORE"
    
print(out,end="")
materiali=int(input())
ore=int(input())
spesa=40*ore+materiali

if spesa<100:
    print("100",end="")
else:
    print(spesa,end="")
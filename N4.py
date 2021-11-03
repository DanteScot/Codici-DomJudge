n=int(input())
if n<0 or n>30:
    print("VOTO NON VALIDO",end="")
elif n>=18:
    print("ESAME SUPERATO",end="")
else:
    print("BOCCIATO",end="")
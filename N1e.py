saldo=int(input())
canone=int(input())
interessi=int(input())

x=saldo

saldo-=canone
saldo=saldo+((saldo*interessi)/100)
saldo=round(saldo)
y=saldo

saldo-=canone
saldo=saldo+((saldo*interessi)/100)
saldo=round(saldo)
z=saldo

print("PRIMO MESE:",x)
print("SECONDO MESE:",y)
print("TERZO MESE:",z,end="")
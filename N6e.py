brisc=int(input())
sem1=int(input())
cart1=int(input())
sem2=int(input())
cart2=int(input())

if cart1==1:
    cart1=12
if cart1==3:
    cart1=11

if cart2==1:
    cart2=12
if cart2==3:
    cart2=11

if sem1==brisc and sem2 !=brisc:
    print("VINCE GIOCATORE 1", end="")
elif sem2==brisc and sem1 !=brisc:
    print("VINCE GIOCATORE 2", end="")
elif sem1!=sem2:
    print("VINCE GIOCATORE 1", end="")
else:
    if cart1>cart2:
        print("VINCE GIOCATORE 1", end="")
    else:
        print("VINCE GIOCATORE 2", end="")
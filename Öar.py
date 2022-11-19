Försvinnanden = []

antalDeltagare = int(input("Antal Deltagare: "))
antalÖar = 0
while True:
    antalÖar += 1
    if len(Försvinnanden) == 0:
        antalDeltagare-= 1
        Försvinnanden.append(1)
    elif len(Försvinnanden) == 1:
        antalDeltagare-= Försvinnanden[0]
        Försvinnanden.append(1)
    else:
        förs = (Försvinnanden[len(Försvinnanden)-1]+Försvinnanden[len(Försvinnanden)-2])
        antalDeltagare -= förs
        Försvinnanden.append(förs)
        
    if antalDeltagare<=0:
        break
print(antalÖar)
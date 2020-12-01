città = []
tmax = []
tmin = []
escursioni = []
ncittà = int(input("quante sono le città"))
escu = int(input("Quale è l'escursione termica?"))
c = 0
for n in range(1,ncittà + 1):
    nomeci = input("quale è la città?")
    tempemassima = float(input("quale è la temperatura massima?"))
    tempeminima = float(input("quale è la temperatura minima?"))
    escursione = tempemassima - tempeminima
    città.append(nomeci)
    tmax.append(tempemassima)
    tmin.append(tempeminima)
    
    if escursione > c:
        c += 1
        
    else:
        print()
print(città)
print(c)
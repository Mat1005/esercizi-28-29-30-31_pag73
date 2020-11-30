partecipanti = []
lanci = []
totpartecipanti = int(input("quanti sono i partecipanti?")
for n in range(1, totpartecipanti +1):
    partecipante = input("nome partecipante")
    lancio = float(input(" quanto è stato il lancio"))
    partecipanti.append(partecipante)
    lanci.append(lancio)
print(partecipanti)
print(lanci)
print(max(lanci))    

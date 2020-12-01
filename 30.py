
    

c = 1
numero = []
potenza = 2
lunghezza = int(input("Quante cifre compongono il numero binario?"))
print("Ora dovrai inserire le cifre(0 o 1) da destra ")
cifra = int(input("inserisci la cifra: "))
if cifra == 1:
    prodotto = cifra
    numero.append(prodotto)
while True:
    if c == lunghezza:
        break
    else:  
        cifra = int(input("inserisci la cifra successiva: "))
        c = c + 1
        if cifra == 1:
            prodotto = cifra*potenza
            numero.append(prodotto)
        potenza = potenza*2
print("Il numero decimale corrispondente al numero binario preso in considerazione è", sum(numero)) 
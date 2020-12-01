cifre = []
resti = []
contatore = -1
numero = int(input("inserire il numero decimale che si vuole convertire in binario."))
while True:
    if numero == 0:
        break
    else:     
        resto = numero % 2
        resti.append(resto)        
        numero = numero//2
resti.reverse()
restitot = len(resti)-1
while True:    
    potenza = pow(10, restitot)
    cifra = resti[contatore +1] * potenza
    restitot = restitot - 1 
    contatore = contatore + 1
    cifre.append(cifra)
    if restitot == -1:
        break
numerobinario = sum(cifre)
print("Il numero binario equivalente al numero decimale ",numero,"è il numero",numerobinario)    

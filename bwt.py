import sys
FINE = "$"

def bwt(testo):
    if FINE in testo:
        print("Errore: la stringa non deve contenere il carattere $")
    if testo=="":
        print("La stringa non può essere vuota")

    testo = testo+FINE

    rotazioni = []
    for i in range(len(testo)):
        rotazioni.append(testo[i:]+testo[:i])
        rotazioni.sort()

    risultato = ""

    for riga in rotazioni: 
        risultato = risultato + riga[-1]
    
    print("BWT:", risultato)

    stringa = input("Inserisci una stringa: ")
    bwt(stringa)

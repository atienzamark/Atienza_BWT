import socket
from bwt import bwt

HOST="127.0.0.1"
PORT=5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()
print("Server in ascolto sulla porta: ", PORT)

while True:

    connessione, indirizzo = server.accept()
    print("Connesione con: ", indirizzo)

    dati = connessione.recv(4096)
    stringa = dati.decode()
    print("Ricevuto: ", stringa)

    risposta = bwt(stringa)

    if risposta == "":
        risposta = "Errore: stringa non valida"

    connessione.sendall(risposta.encode())
    print("Inviato: ", risposta)
    
    connessione.close()
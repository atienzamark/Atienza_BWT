import socket

HOST="127.0.0.1"
PORT=5050

stringa = input("Inserisci la stringa: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.sendall(stringa.encode())

risposta = client.recv(4096).decode()
print("BWT ricevuta: ", risposta)

client.close()
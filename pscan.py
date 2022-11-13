
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.05)

IP = input("Digite o host ou ip: ")
PORT = int(input("Qual é a porta a ser mapeada ? "))

code = client.connect_ex((IP, PORT))

if code == 0:
    print("Porta Aberta")
else:
    print("Porta Fechada")



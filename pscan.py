# Biblioteca para comunicação da placa de rede

import socket

IP = input("Digite o host ou ip a ser verificado: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input("Qual é a porta a ser mapeada? ")))
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((IP, port))

    if code == 0:
        print(str(port), " -> Porta Aberta")
    else:
        print(str(port), " -> Porta Fechada")

print("Scan Finalizado !")

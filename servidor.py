import socket

chatOnline = False

host = '127.0.0.1'
port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
server_socket.settimeout(30)

print("Servidor iniciado. Aguardando conexão...")

try:
    client_socket, client_address = server_socket.accept()
    print(f"Conectado com {client_address}")
    chatOnline = True
except socket.timeout:
    print("Tempo de espera excedido. Encerrando o servidor...")
    server_socket.close()
    exit()

while chatOnline:
    data_to_send = input("Você: ")
    client_socket.send(data_to_send.encode())
    if data_to_send.lower() == 'sair':
        chatOnline = False
        continue

    received_data = client_socket.recv(1024)
    if (not received_data) or (received_data.decode().lower() == 'sair'):
        print("O cliente encerrou a conexão. Encerrando o chat...")
        chatOnline = False
        continue

    print(f"Cliente: {received_data.decode()}")

client_socket.close()
server_socket.close()

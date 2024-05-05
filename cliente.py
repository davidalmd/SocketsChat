import socket
import time

chatOnline = False
serverOnline = False
timeout = 30
start_time = None

host = '127.0.0.1'
port = 8080

while not serverOnline and (start_time is None or (time.time() - start_time < timeout)):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        serverOnline = True
        chatOnline = True

        print(f"Conectado ao servidor {host} pela porta {port}. Aguarde a mensagem para começar a conversar...")

    except ConnectionRefusedError:
        print(f"O servidor não está disponível. Tentando novamente...")
        time.sleep(2)
        if start_time is None:
            start_time = time.time()

if not serverOnline:
    print(f"O servidor {host} pela porta {port} não está disponível. Tente novamente mais tarde.")
    exit()

while chatOnline:
    received_data = client_socket.recv(1024)
    if (not received_data) or (received_data.decode().lower() == 'sair'):
        print("O servidor encerrou a conexão. Encerrando o chat...")
        chatOnline = False
        continue

    print(f"Servidor: {received_data.decode()}")

    data_to_send = input("Você: ")
    client_socket.send(data_to_send.encode())
    if data_to_send.lower() == 'sair':
        chatOnline = False
        continue

client_socket.close()

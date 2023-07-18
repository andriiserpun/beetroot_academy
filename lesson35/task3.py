import socket
import threading
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("Получено сообщение от клиента:", request.decode())
    client_socket.send(request)
    client_socket.close()
def start_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Сервер запущен на порту", port)

    while True:
        client_socket, addr = server_socket.accept()
        print("Получено ноаое подключение от", addr)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


start_server()

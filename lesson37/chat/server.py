import socket
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432
separator = "<SEP>"

client_sockets = set()


def filter_message(message):
    return message

def listen_message(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
        except Exception as e:
            print("!!! ERROR", e)
            client_sockets.remove(client)
        else:
            message = message.replace(separator, ": ")
        for cl in client_sockets:
            cl.send(message.encode("utf-8"))
def listen_message(connection):
    while True:
        message = connection.recv(1024).decode("utf-8")
        filtered_message = filter_message(message)
        print(f"message: {filtered_message}")
def is_nickname_unique(nickname):
    for used_nickname in nickname:
        if used_nickname == nickname:
            return False
    return True

def handle_client(client_socket, client_address):
    while True:
        try:
            nickname = client_socket.recv(1024).decode("utf-8")
            if is_nickname_unique(nickname):
                nickname.add(nickname)
                print(f"*** New client {client_address} connected with the nickname: {nickname}")
                break
            else:
                client_socket.send("Nickname is already taken. Please choose a different one.".encode("utf-8"))
        except Exception as e:
            print("!!! ERROR", e)
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"*** Listening as {SERVER_HOST}:{SERVER_PORT}")
    while True:
        client_socket, client_address = s.accept()
        print(f"*** Connected a new client {client_address}")
        client_sockets.add(client_socket)
        thread = threading.Thread(target=listen_message, args=(client_socket,), daemon=True)
        thread.start()



import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init

init()
colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
client_color = random.choice(colors)
censor_words = ["bad_word1", "bad_word2", "bad_word3", "bad_word4"]
used_nicknames = set()

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432
separator = "<SEP>"

def listen_message(connection):
    while True:
        message = connection.recv(1024).decode("utf-8")
        print(f"message: {message}")

def filter_message(message):
    for word in censor_words:
        if word in message:
            message = message.replace(word, "*" * len(word))
    return message

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"*** Connecting to {SERVER_HOST}:{SERVER_PORT} . . .")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("*** Connected!")
    name = input("Please, enter your nickname: ")
    thread = Thread(target=listen_message, args=(s,), daemon=True)
    thread.start()
    while True:
        message = input()
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{client_color}[{ts}]{name}{separator}{message}{Fore.RESET}"
        s.send(message.encode("utf-8"))


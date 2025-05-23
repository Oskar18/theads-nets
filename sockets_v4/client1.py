import socket
import threading


HOST = '127.0.0.1'
PORT = 12345


def receive_messages(client_socket):
    """Prijíma správy od servera."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break


def main():
    """Hlavná funkcia na spustenie klienta."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Pripojený k serveru. Môžete začať chatovať.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


if __name__ == "__main__":
 main()
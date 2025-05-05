import socket

# Vytvoření klientského soketu
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

while True:
    message = input("Zadejte zprávu (nebo 'exit' pro ukončení): ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
    response = client_socket.recv(1024).decode()
    print(f"Server odpověděl: {response}")

client_socket.close()

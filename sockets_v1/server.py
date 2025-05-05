import socket

# Vytvoření serverového soketu
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
print("Server čeká na připojení...")

conn, addr = server_socket.accept()
print(f"Připojení od: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        break
    print(f"Klient: {data}")
    conn.send(f"Server přijal: {data}".encode())

conn.close()
server_socket.close()

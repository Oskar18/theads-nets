import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    country = input("Enter Country: ")
    city = input("Enter City: ")
    client_socket.sendall(f"{country},{city}".encode())

    weather = client_socket.recv(1024).decode()
    print(f"Weather in {city}, {country}: {weather}")
    client_socket.close()


start_client()
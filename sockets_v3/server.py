import socket
import threading


def read_weather_data():
    weather_info = {}
    with open('weather_data.txt', 'r') as file:
        for line in file.readlines():
            country, city, weather = line.strip().split(',')
            weather_info[(country, city)] = weather
    return weather_info


def handle_client(client_socket, weather_info):
    try:
        request = client_socket.recv(1024).decode().strip().split(',')
        country, city = request[0], request[1]
        weather = weather_info.get((country, city), "No data available")
        client_socket.sendall(weather.encode())
    finally:
        client_socket.close()


def start_server():
    weather_info = read_weather_data()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()

    print("Weather Server is listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, weather_info))
        client_thread.start()


start_server()
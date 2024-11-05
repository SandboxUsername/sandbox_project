import socket
import os
# from dotenv import load_dotenv

# load_dotenv()

host, port = os.getenv('HOST'), os.getenv('PORT')
host, port = 'localhost', 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")
    while True:
        message = input('Client: ')
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        if not response or response.lower() == 'exit':
            break
        print(f"Server: {response}")
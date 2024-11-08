import socket
import os
from dotenv import load_dotenv

load_dotenv()
host, port = 'localhost', 12345
host, port = 'localhost', int(os.getenv('PORT'))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")
    
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            break
        print(f'Client: {data}')
        response = input('Server: ')
        if response == 'exit':
            break
        conn.send(response.encode())

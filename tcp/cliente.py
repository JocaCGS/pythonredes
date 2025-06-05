import socket

def start_client(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = input('Type your message: ')
    
    while message != 'exit':
        client_socket.sendall(message.encode('utf-8'))
        message = input('Type your message: ')

    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8000

    start_client(HOST, PORT)

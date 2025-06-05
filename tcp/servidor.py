import socket

def start_server(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    
    server_socket.listen(1)

    print(f'Servidor iniciado em {host}:{port}')


    while True:
        client_socket, address = server_socket.accept()

        while True:

            data = client_socket.recv(1024)

            if not data:
                print('Cliente desconectou')
                client_socket.close()
                server_socket.close()
                return

            message = data.decode('utf-8')

            print(f'[CLIENTE]: {message}' )

            
            if message == 'exit':
                print('Servidor encerrado pelo cliente')
                client_socket.close()
                server_socket.close()
                return


        


if __name__=='__main__':
    HOST = 'localhost' # ENDEREÇO IP DO SERVIDOR
    PORT = 8000 # PORTA DO SERVIDOR



start_server(HOST,PORT)
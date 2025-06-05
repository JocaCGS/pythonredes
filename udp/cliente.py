import socket

def send_message(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.sendto(message, (host,port))


if __name__=='__main__':
    HOST = 'localhost' # ENDEREÇO IP DO SERVIDOR
    PORT = 9000 # PORTA DO SERVIDOR

    while True:
        message = input('Type your message: ').encode('utf-8')
        
        send_message(HOST,PORT)
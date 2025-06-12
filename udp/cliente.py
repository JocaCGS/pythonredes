import socket

def send_message(host: str, port: int, message:str):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.sendto(message, (host,port))




if __name__=='__main__':
    HOST = '10.20.22.186' # ENDEREÇO IP DO SERVIDOR
    PORT = 9000 # PORTA DO SERVIDOR

    name = input('Enter your name: ')
    

    while True:
        message = input('Type your message: ')

        body_message = f"{name}!={message}".encode('utf-8')   
        send_message(HOST,PORT, body_message)
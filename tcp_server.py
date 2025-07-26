import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address) 
    server_socket.listen(5)
    print('Server runing. Waiting connect')
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connecting in {client_address}')
        
        data = client_socket.recv(1024).decode()
        print(f'Get message: {data}')
        
        response = f'Server getting: {data}'
        client_socket.send(response.encode())
        client_socket.close()
        
if __name__ == '__main__':
    server()
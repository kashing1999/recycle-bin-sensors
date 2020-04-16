import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        choice = input('Enter choice')
        if not choice.isdigit():
            continue
        if choice=='4':
            break
		if  choice =='5':
            s.sendall( (choice.encode()))
            break
        s.sendall( (choice.encode()))
        data = s.recv(1024)
        
        print('Received', data.decode())

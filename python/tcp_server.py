import socket

IP = ''
PORT = 1337

# Start a socket object using IPv4 propertie and TCP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to our local pc on IP 0.0.0.0, port 1337
sock.bind((IP, PORT))
# Start listening with a backlog size of 10
sock.listen(10)

# Indicates if we have a connection
connection = False

# Check if we have a connection (or not), print waiting statement while False
while True:
    if connection is False:
        print('Waiting for connection')
        connection, client = sock.accept()
        print('Connection from', client)
    else:
        received = connection.recv(1024)
        received_message = received.decode('utf-8')
        print('[RECEIVED]: ' + received_message)
        connection.send(str.encode(received_message))
        
        
socket.close()
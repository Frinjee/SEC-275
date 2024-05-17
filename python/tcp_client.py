import socket

IP = ''
PORT = 1337

# Create TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
sock.connect((IP, PORT))

print('Connected')

# Start a loop to send and receive messages
while True:
    message = input('[SEND]: ')
    sock.send(str.encmessage)
    received = sock.recv(1024)
    print(received.decode('utf-8'))
    
socket.close()

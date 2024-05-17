import socket

HOST = ''
PORT = 1337

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((HOST, PORT))

print('Waiting for incoming data')

while True:
    received, address = soc.recvfrom(1024)
    received_message = received.decode('utf-8')
    
    print('[RECEIVED]: ' + received_message.strip())
    
    soc.sendto(str.encode(received_message), address)

socket.close()
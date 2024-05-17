import socket

HOST = ''
PORT = 1337

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Ready')

while True:
    message = input('[SEND]: ')
    soc.sendto(str.encode(message), (HOST, PORT))
    
    received = socket.recvfrom(1024)
    print(received[0].decode('utf-8'))
    
socket.close()
 
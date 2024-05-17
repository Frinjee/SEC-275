import socket, threading, os

SERVER_HOST = ''
SERVER_PORT = 1337
BUFFER_SIZE = 4096
SEPARATOR = '<SEPARATOR>'


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((SERVER_HOST, SERVER_PORT))
soc.listen(5)

print(f'[*] Listening as {SERVER_HOST}:{SERVER_PORT}')

def client_handler(client_soc):
    while True:
        cmd = client_soc.recv(BUFFER_SIZE).decode()
        if not cmd: break
        
        cmd = cmd.split()
        if cmd[0] == 'UPLOAD':
            f_name = cmd[1]
            f_size =int(cmd[2])
            
            with open(f_name, 'wb') as f:
                read_bytes = client_soc.recv(BUFFER_SIZE)
                while read_bytes:
                    f.write(read_bytes)
                    if len(read_bytes) < BUFFER_SIZE: break
                    read_bytes = client_soc.recv(BUFFER_SIZE)
                print(f'[*] UPLOADED {f_name} {f_size}')
                
        elif cmd[0] == 'DOWNLAOD':
            f_name = cmd[1]    
            if os.path.exists(f_name):
                f_size = os.path.getsize(f_name)
                client_soc.send(f'{f_name}{SEPARATOR}{f_size}'.encode())
                
                with open(f_name, 'rb') as f:
                    read_bytes = f.read(BUFFER_SIZE)
                    while read_bytes:
                        client_soc.send(read_bytes)
                        read_bytes = f.read(BUFFER_SIZE)
                print(f'[*] SENT {f_name}')
            
            else:
                client_soc.send(b'ERROR: FILE NOT FOUND')
                
        else:
            client_soc.send(b'ERROR: INVALID COMMAND')
    client_soc.close()
    
while True:
    client_soc, address = soc.accept()
    print(f'[+] {address} connected')
    handler = threading.Thread(target=client_handler, args=(client_soc,))
    handler.start()
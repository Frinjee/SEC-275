import socket, os
import tkinter as tk
from tkinter import filedialog

SERVER_HOST = ''
SERVER_PORT = 1337
BUFFER_SIZE = 4096
SEPARATOR = '<SEPARATOR>'

def file_upload(f_path):
    f_name = os.path.basename(f_path)
    f_size = os.path.getsize(f_path)
    client_soc.send(f"UPLOAD {f_name} {f_size}".encode())

    with open(f_path, "rb") as f:
        bytes_read = f.read(BUFFER_SIZE)
        while bytes_read:
            client_soc.send(bytes_read)
            bytes_read = f.read(BUFFER_SIZE)
    print(f"[*] Uploaded {f_name}")
    
def file_download(f_name):
    client_soc.send(f'DOWNLOAD {f_name}'.encode())
    res = client_soc.recv(BUFFER_SIZE).decode()
    
    if res.startswith("ERROR"):
        print(res)
        return
    
    f_name, f_size = res.split(SEPARATOR)
    f_size = int(f_size)
    
    with open(f_name, 'wb') as f:
        read_bytes = client_soc.recv(BUFFER_SIZE)
        while read_bytes:
            f.write(read_bytes)
            if len(read_bytes) < BUFFER_SIZE: break
            read_bytes = client_soc.recv(BUFFER_SIZE)
    print(f'[*] DOWNLOADED {f_name}')
    
client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_soc.connect((SERVER_HOST, SERVER_PORT))



def main():
    print('COMMANDS: \nUPLOAD, \nDOWNLOAD, \nEXIT')
    while True:
        command = input("> ").strip().split()
        if not command: continue

        if command[0].upper() == "UPLOAD":
            root = tk.Tk()
            root.withdraw()  
            f_path = filedialog.askopenfilename()
                
            if f_path:
                file_upload(f_path)
            else: print('ERROR: FILE NOT FOUND')
                    
        elif command[0].upper() == "DOWNLOAD":
            if len(command) > 1:
                f_name = command[1]
                root = tk.Tk()
                root.withdraw()
                save_directory = filedialog.askdirectory()
                    
                if save_directory:
                    file_download(f_name, save_directory)
                else:
                    print("ERROR: NO FILE NAME PROVIDED")
                
        elif command[0].upper() == "EXIT":
            client_soc.close()
            break
        
        else:
            print("INVALID COMMAND")
            
if __name__ == "__main__":
    main()          
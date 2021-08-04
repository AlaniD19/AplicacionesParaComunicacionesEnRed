import os
import socket
import pathlib
import sys
import shutil
from pathlib import Path

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('conectado a {} puerto {}'.format(*server_address))
sock.connect(server_address)
# Folder de archivos local
folder = 'tucarpetita'

def my_folder(dir):
    directorio = pathlib.Path(dir)
    print('/'+str(directorio)+'/')
    for fichero in directorio.iterdir():
        if fichero.is_dir():
            folder = str(fichero.name)+'/'
            print('\t', folder)
        else:
            print('\t', fichero.name)
def up_file(name):
    os.chdir(folder)
    file = open(name, "rb")
    data = file.read(1024)
    print("Subiendo...")
    while data:
        sock.send(data)
        data = file.read(1024)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    os.chdir('..')
    sock.send(b"DONE")
    print(name, "cargado en wugul draif")
def up_folder(name):
    os.chdir(folder)
    shutil.make_archive(name, "zip", name)
    file = open(name+'.zip', "rb")
    data = file.read(1024)
    print("Subiendo...")
    while data:
        sock.send(data)
        data = file.read(1024)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    os.unlink(name+'.zip')
    os.chdir('..')
    sock.send(b"DONE")
    print(name, "enviado a wugul draif")
def down_file(name):
    os.chdir(folder)
    file = open(name, "wb")
    print("Descargando...", name)
    while True:
        data = sock.recv(1024)
        if data == b"DONE":
            print(name, "descargado \n")
            sys.stdin.flush()
            break
        file.write(data)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    os.chdir('..')
def down_folder(name):
    os.chdir(folder)
    os.makedirs(name)
    os.chdir(name)
    file = open(name + '.zip', "wb")
    print("Descargando carpeta...", name)
    while True:
        data = sock.recv(1024)
        if data == b"DONE":
            print("Descarga completa. \n")
            sys.stdin.flush()
            break
        file.write(data)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    shutil.unpack_archive(name + '.zip')
    os.unlink(name + '.zip')
    os.chdir('..')
    os.chdir('..')
def del_file(name):
    while True:
        data = sock.recv(1024)
        if data == b'DONE':
            print(name, 'eliminado de wugul draif')
            sys.stdin.flush()
            break
    sys.stdin.flush()
def del_folder(name):
    while True:
        data = sock.recv(1024)
        if data == b'DONE':
            print(name, 'eliminada de wugul draif')
            sys.stdin.flush()
            break
    sys.stdin.flush()

try:
    while True:
        # os.system('cls')
        sys.stdin.flush()
        data = sock.recv(1024)
        print('\n')
        my_folder(folder)
        print('\n', data.decode())

        request = input('>>> ')
        sock.sendall(request.encode())
        if request == '1':
            print('\nque archivo subimos crack?')
            name = input('>>> ')
            sock.sendall(name.encode())
            up_file(name)
        elif request == '2':
            print('\nque carpeta subimos crack?')
            name = input('>>> ')
            sock.sendall(name.encode())
            up_folder(name)
        elif request == '3':
            print('\nque archivo descargamos crack?')
            name = input('>>> ')
            sock.sendall(name.encode())
            down_file(name)
        elif request == '4':
            print('\nque carpeta descargamos crack?')
            name = input('>>> ')
            sock.sendall(name.encode())
            down_folder(name)
        elif request == '5':
            print('\nque archivo eliminamos crack?')
            name = input('>>> ')
            sock.sendall(name.encode())
            del_file(name)
        elif request == '6':
            print('\nque carpeta eliminamos crack?')
            name = input('>>> ')
            sock.sendall(name.encode())
            del_folder(name)
        else:
            break
finally:
    sock.close()
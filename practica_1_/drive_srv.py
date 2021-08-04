import socket
import pathlib
import os
import sys
import shutil

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('iniciando servicio {} en puerto {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
# carpeta del servidor
folder = 'drive'

def server_directory(path):
    data = b'WUGUL DRAIF >>> \n'
    directorio = pathlib.Path(path)
    for fichero in directorio.iterdir():
        if fichero.is_dir():
            data += b'\t '
            data += bytes(fichero.name, encoding="utf-8")
            data += b'/ \n'
        else:
            data += b'\t '
            data += bytes(fichero.name, encoding="utf-8")
            data += b'\n'
    return data
menu = b'''\n\n##########     ACCIONES     ##########
    1 >> Subir archivo
    2 >> Subir carpeta
    3 >> Descargar archivo
    4 >> Descargar carpeta
    5 >> Eliminar archivo (Wugul)
    6 >> Eliminar carpeta (Wugul)
    X >> Terminar conexion
'''

def up_file(name):
    file = open(name, "wb")
    print("Recibiendo....", name)
    while True:
        data = connection.recv(1024)
        if data == b"DONE":
            print("Carga completa. \n")
            sys.stdin.flush()
            break
        file.write(data)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    os.chdir('..')
def up_folder(name):
    os.makedirs(name)
    os.chdir(name)
    file = open(name+'.zip', "wb")
    print("Recibiendo....", name)
    while True:
        data = connection.recv(1024)
        if data == b"DONE":
            print("Carga completa. \n")
            sys.stdin.flush()
            break
        file.write(data)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    shutil.unpack_archive(name+'.zip')
    os.unlink(name + '.zip')
    os.chdir('..')
    os.chdir('..')
def down_file(name):
    file = open(name, "rb")
    data = file.read(1024)
    print("Enviando...", name)
    while data:
        connection.send(data)
        data = file.read(1024)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    os.chdir('..')
    connection.send(b"DONE")
    print("Enviado correctamente")
def down_folder(name):
    shutil.make_archive(name, "zip", name)
    file = open(name + '.zip', "rb")
    data = file.read(1024)
    print("Enviando...", name)
    while data:
        connection.send(data)
        data = file.read(1024)
        sys.stdin.flush()
    sys.stdin.flush()
    file.close()
    os.unlink(name + '.zip')
    os.chdir('..')
    connection.send(b"DONE")
    print("Enviado correctamente")
def del_file(name):
    print('Eliminando...', name)
    os.unlink(name)
    print('Archivo eliminado correctamente')
    connection.send(b'DONE')
    os.chdir('..')
def del_folder(name):
    print('Eliminando...', name)
    shutil.rmtree(name)
    print('Carpeta eliminada correctamente')
    connection.send(b'DONE')
    os.chdir('..')

while True:
    print('\nesperando conexion...')
    connection, client_address = sock.accept()
    # connection.setblocking(1)
    try:
        print('\ncliente conectado:', client_address)
        while True:
            sys.stdin.flush()
            directory = server_directory(folder)
            connection.sendall(directory+menu)
            data = connection.recv(5)
            print('accion >>>', data.decode())
            if data:
                os.chdir('drive')
                if data.decode() == '1':
                    name = connection.recv(50)
                    up_file(name.decode())
                    sys.stdin.flush()
                elif data.decode() == '2':
                    name = connection.recv(50)
                    up_folder(name.decode())
                    sys.stdin.flush()
                elif data.decode() == '3':
                    name = connection.recv(50)
                    down_file(name.decode())
                    sys.stdin.flush()
                elif data.decode() == '4':
                    name = connection.recv(50)
                    down_folder(name.decode())
                    sys.stdin.flush()
                elif data.decode() == '5':
                    name = connection.recv(50)
                    del_file(name.decode())
                    sys.stdin.flush()
                elif data.decode() == '6':
                    name = connection.recv(50)
                    del_folder(name.decode())
                    sys.stdin.flush()
                elif data.decode() == 'X':
                    sys.stdin.flush()
                    break
            else:
                break
    finally:
        connection.close()
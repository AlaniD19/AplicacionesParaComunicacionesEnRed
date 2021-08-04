import socket
import sys

# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 3000)
print('conectando a %s puerto %s' % server_address)
sock.connect(server_address)

try:
    # Enviando datos
    message = b' '
    sock.sendall(message)
    # Buscando respuesta
    while True:
        data = sock.recv(512)
        print(data.decode("utf-8"))
        print('')
        level = bytes(str(input('>>> ')), encoding="utf-8")
        sock.sendall(level)

        palabra = sock.recv(254)
        print(palabra.decode("utf-8"))
        while True:
            sys.stdin.flush()
            intento = bytes(str(input('>>>  ')), encoding="utf-8")
            sock.sendall(intento)
            resultado = sock.recv(512)
            print(resultado.decode("utf-8"))
            print()
            if '_' not in resultado.decode("utf-8"):
                break
            elif '0' in resultado.decode("utf-8"):
                break
except:
    print('Fin de conexion...')

finally:
    print('cerrando socket...')
    sock.close()
import socket
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect the socket to the port on the server
# given by the caller
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# buffer size
BUFFER_SIZE = 10

try:
    print('\n\n[Para salir escribe X]]')
    print('Mensaje a enviar:')
    message = input('>>> ')
    print('\nEnviando >> ', message, '\n')
    while message != 'X':
        for i in range (0, len(message)//BUFFER_SIZE+1):
            # preparar paquete con metadata
            package = message[i*BUFFER_SIZE:(i*BUFFER_SIZE)+BUFFER_SIZE]
            data = {
                'id': i,
                'size': len(package),
                'message': package
            }
            sock.sendto(json.dumps(data).encode(), server_address)

            # recibir acuses
            data, server = sock.recvfrom(BUFFER_SIZE)
            print('Recibido >> ', data.decode())

        print('\n\n[Para salir escribe X]')
        print('Mensaje a enviar:')
        message = input('>>> ')
finally:
    sock.close()
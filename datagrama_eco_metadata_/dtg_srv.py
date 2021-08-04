import socket
import json

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address given on the command line
server_name = 'localhost'  # sys.argv[1]
server_address = (server_name, 10000)
print('Conexion con {} en {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nEsperando por mensaje...')
    data, address = sock.recvfrom(4096)

    if data:
        query = json.loads(data.decode())
        print('Recibiendo {} bytes de {}'.format(query['size'], address))
        print('id >> ', query["id"])
        print('package >> ', query["message"])
        sent = sock.sendto(str.encode(query["message"]), address)
        print('Enviando {} bytes a {}'.format(sent, address))
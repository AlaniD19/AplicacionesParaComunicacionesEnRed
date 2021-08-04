import socket
import json
import sys
import threading
import os

# Lists for control of users in the session
users = []
usr_id = []


# function for thread recv data to chat udp
def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    os.system('cls')
    server_address = ('localhost', 10000)
    print('--- Starting server in: {} port: {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        # Received data
        data, address = sock.recvfrom(4096)
        query = json.loads(data.decode())

        # New user join the server
        if query.get('type') == 0:
            users.append(query.get('port'))
            usr_id.append(query.get('user'))
            s_sender = threading.Thread(target=sender, args=(str(usr_id), 'server', 3, query.get('port')))
            s_sender.start()
            print('\n[]+ {} in {} has join the session\n'.format(query.get('user'), address))

        # Message to multicast group
        elif query.get('type') == 1:
            print('>>> Message received and send to multicast group from: {}'.format(address))
            s_sender = threading.Thread(target=sender, args=(query.get('message'), query.get('user'), 1, ''))
            s_sender.start()

        # User left the server
        elif query.get('type') == 2:
            print('\n[]- {} in {} has left the session'.format(query.get('user'), address))
            s_sender = threading.Thread(target=sender, args=(query.get('message'), query.get('user'), 2, ''))
            s_sender.start()
            users.remove(query.get('port'))
            usr_id.remove(query.get('user'))
        else:
            pass


# thread sender function
def sender(msg, usr, typ, prt):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if typ == 1 or typ == 2 or typ == 0:
        multicast = {
            'message': msg,
            'user': usr,
            'type': typ,
            'port': ''
        }
        for i in users:
            sock.sendto(json.dumps(multicast).encode(), ('localhost', i))
    else:
        multicast = {
            'message': msg,
            'user': usr,
            'type': typ,
            'port': ''
        }
        sock.sendto(json.dumps(multicast).encode(), ('localhost', prt))


server_recv = threading.Thread(target=receiver)
server_recv.start()
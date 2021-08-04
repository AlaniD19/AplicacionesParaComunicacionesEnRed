import socket
import json
from time import time
from colorama import init
from termcolor import colored
import os

init(autoreset=True)

# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 3000)
print('conectando a %s puerto %s' % server_address)
sock.connect(server_address)

def verify_cordinates(coordenada, solucion):
    cordinate = []
    for x in coordenada:
        if x.isdigit():
            cordinate.append(int(x))
        else:
            return '', False
    for key in solucion:
        if cordinate == solucion[key]:
            return key, True
    return '', False

try:
    os.system("cls")
    # Enviando datos
    message = b' '
    sock.sendall(message)
    # Buscando respuesta
    while True:
        # Recibimos los datos para jugar
        topic = sock.recv(128)
        tablero = sock.recv(2048).decode()
        solve = json.loads(sock.recv(1024).decode())
        # definimos la listas de solucion
        words = []
        words_finder = []
        for key in solve:
            words.append(key)

        # jugamos hasta que no queden palabras en cola
        time_s = time()
        while words:
            os.system("cls")
            # imprimimos el topico de la sopa de letras
            print('\n\t TOPICO >>> ', colored(topic.decode("utf-8").upper(), 'green'), '\n')
            # dibujamos el tablero recibido
            print(tablero)
            # mostramos palabras a encontrar
            print('PODRAS ENCONTRAR ESTAS PALABRAS CRACK?...')
            for i in words:
                print(colored(i, 'blue'), end='    ')
            # mostramos las palabras que hemos encontrado
            print('\n\nPALABRAS ENCONTRADAS CRACK...')
            if not words_finder:
                print(colored('Nada aun capo, piensa esponja, piensa...', 'cyan'), end='\t')
            else:
                for i in words_finder:
                    print(colored(i, 'cyan'), end='    ')
            # preguntas por las coordenadas
            print('\n\nintroduce las cordenadas de la primera y ultima letra de la palabra, por espacios')
            print('ejemplo : 1 2 3 4')
            word_try = list(input('algunas cordenadas crack? >>> ').split())
            # comprobamos si las cordenadas son validas
            llave, resultado = verify_cordinates(word_try, solve)
            if resultado:
                words_finder.append(llave)
                words.remove(llave)
            else:
                pause = input(colored('\nUy no capo, si ves bien o te presto mis lestes?...', 'red'))

        # cuando el juego finalize enviamos el tiempo que le tomo al jugador
        time_f = time()
        sock.sendall(bytes(str(time_f-time_s), encoding='utf-8'))

        print(colored('\n\nGRANDEEE!!! TU NOMBRE SERA RECORDADO POR LAS GENERACIONES!...', 'red'))
except:
    print('')

finally:
    print('cerrando socket...')
    sock.close()
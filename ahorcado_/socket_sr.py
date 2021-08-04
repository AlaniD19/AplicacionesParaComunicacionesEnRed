import random
import socket
from time import time
import sys
from datetime import datetime


def bienvenida():
    return b'''
    ******************************
        EL AHORCADO - THE GAME
    ******************************
    QUE DIFICUALTAD CRACK?
    1- EASY
    2- SEMIPRO
    3- DIOS DEL OLIMPO'''


def start_game(level):
    print('Juego Iniciado...')
    if level == b'1':
        diccionario = ['casa', 'hola', 'roma']
        vidas = 2
    elif level == b'2':
        diccionario = ['pescado', 'calamar', 'monigote']
        vidas = 4
    else:
        diccionario = ['otorrinolaringologo', 'parangaricutirimicuaro', 'elparaquecosadequien']
        vidas = 6
    palabra = random.choice(diccionario).lower()
    print('Palabra en juego >>> ', palabra)
    tablero = '_ ' * len(palabra)
    return palabra, tablero, vidas


def word_refresh(palabra, letra, tablero, lifes):
    letter = str(letra, encoding="utf-8")
    refresh = tablero.split()
    for indice, letra_palabra in enumerate(palabra):
        if letter == letra_palabra:
            refresh[indice] = letter
    if letter not in palabra:
        lifes -= 1
    result = ' '.join(refresh)
    return result, lifes


def verify(palabra, tablero):
    formateo = ''.join(tablero.split())
    if palabra == formateo:
        return True
    else:
        return False


# Creando el socket TCP/IP (IPv4)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ('localhost', 3000)
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen()

while True:
    # Esperando conexion
    print('Esperando para conectarse...')
    connection, client_address = sock.accept()
    try:
        print('concexion desde', client_address)
        data = connection.recv(1)
        # Recibe datos y reetransmite
        connection.sendall(bienvenida())
        level = connection.recv(32)
        palabra, tablero, vidas = start_game(level)
        game = b'''Intenta adivinar alguna letra crack, aqui esta la palabra
                    ''' + bytes(tablero, encoding="utf-8")
        connection.sendall(game)
        tiempo_inicio = time()
        palabra_adivinada = tablero
        while True:
            if '_' not in palabra_adivinada:
                connection.send(b'Ganaste... Nada mal. \n\n')
                sys.stdin.flush()
                tiempo_final = time()
                puntaje = tiempo_final - tiempo_inicio
                print(puntaje)
                print()
                # registrar puntaje
                f = open('winners.txt', 'a')
                f.write('Jugador >>> ' + str(client_address))
                f.write('\n' + 'Puntaje >>> ' + str(puntaje))
                f.write('\n' + 'Nivel >>> ' + level.decode(encoding="utf-8"))
                f.write('\n' + 'Fecha >>> ' + str(datetime.now()) + '\n\n')
                f.close()
                break
            elif vidas < 1:
                connection.send(b'Game Over my friend :\'u \n\n')
                sys.stdin.flush()
                tiempo_final = time()
                puntaje = tiempo_final - tiempo_inicio
                print(puntaje)
                print()
                break
            sys.stdin.flush()
            letra = connection.recv(8)
            # print(letra)
            palabra_adivinada, vidas = word_refresh(palabra, letra, palabra_adivinada, vidas)
            # print(palabra_adivinada)
            avance = bytes(palabra_adivinada, encoding="utf-8") + b'''
            Vidas: ''' + bytes(str(vidas), encoding="utf-8")
            connection.sendall(avance)
    finally:
        # Cerrando conexion
        connection.close()

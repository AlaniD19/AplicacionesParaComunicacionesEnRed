import random
from datetime import datetime
import numpy as np
import socket
import json


def start_game():
    class Cursor:
        def __init__(self, fila, columna):
            self.fila = fila
            self.columna = columna
            self.avanX = [-1, 0, 1][random.randint(0, 2)]
            self.avanY = [-1, 0, 1][random.randint(0, 2)]
            if self.avanX == 0 and self.avanY == 0:
                self.avanX = 1

        def next(self, pasos=1):
            self.fila += pasos * self.avanX
            self.columna += pasos * self.avanY

        def es_valido(self, dimension):
            return 0 <= self.fila < dimension and 0 <= self.columna < dimension

        def __str__(self):
            return f"[{self.fila} {self.avanX}, {self.columna} {self.avanY}]"
    class Matrix:
        def __init__(self, dimension):
            valores = [' '] * dimension * dimension
            self.dimension = dimension
            self.matriz = np.array(valores).reshape((dimension, dimension))
            self.libres = dimension * dimension
            self.palabras = {}

        def __getitem__(self, cursor):
            if cursor.es_valido(self.dimension):
                return self.matriz[cursor.fila][cursor.columna]
            else:
                return ' '

        def __setitem__(self, cursor, value):
            if cursor.es_valido(self.dimension):
                if self.matriz[cursor.fila][cursor.columna] == ' ':
                    self.libres -= 1
                self.matriz[cursor.fila][cursor.columna] = value

        def put(self, palabra):
            x, y = random.randint(0, self.dimension - 1), random.randint(0, self.dimension - 1)
            cursor = Cursor(x, y)

            largo = len(palabra)
            cursor.next(largo)
            if not cursor.es_valido(self.dimension):
                return False
            cursor.next(-largo)

            restantes = largo
            for indice in range(largo):
                if self[cursor] == ' ' or self[cursor] == palabra[indice]:
                    self[cursor] = palabra[indice]
                    restantes -= 1
                cursor.next()

            if restantes == 0:
                # Esta palabra aparece completa en la matriz
                self.palabras[palabra] = [x, y, cursor.fila-cursor.avanX, cursor.columna-cursor.avanY]

            return True

        def __str__(self):
            regla = f"   {('0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15')} \n" #* int(self.dimension))[:self.dimension * 2]}\n"
            linea = regla
            for i in range(self.dimension):
                linea += f"{i:2d} {'  '.join(self.matriz[i].tolist())}\n"
            return linea + regla

    def verify_word(palabra):
        for i in range(len(matriz.palabras)):
            if palabra in matriz.palabras.values():
                return True
            else:
                return False

    print('Juego Iniciado...')
    theme = b''
    # DIM = 16  # tamaño del tablero
    matriz = Matrix(16)
    # eleccion aleatoria del topico de la sopa de letras
    topic = random.choice([1, 2, 3])
    if topic == 1:
        theme = b'Animales'
        palabras = [
            'leon', 'tiburon', 'jaguar', 'tucan', 'lobo', 'cocodrilo', 'armadillo', 'pollo',
            'oveja', 'jirafa', 'aguila', 'ballena', 'golondrina', 'serpiente', 'tortuga',
            'zorro', 'pantera', 'avestruz', 'beluga', 'caballo', 'calamar', 'cangrejo',
            'delfin', 'elefante', 'escorpion', 'gacela', 'gorila', 'hipopotamo', 'impala',
            'koala', 'langosta', 'lechuza', 'mapache', 'marmota', 'medusa', 'murcielago',
            'ocelote', 'pajaro', 'paloma', 'percebe', 'mantaraya', 'ajolote', 'salamandra',
            'coyote', 'perezoso', 'urraca'
        ]
        while matriz.libres:
            palabra = palabras[random.randint(0, len(palabras) - 1)]
            if verify_word(palabra):
                palabras.remove(palabra)
            else:
                largo = len(palabra)
                matriz.put(palabra)
    elif topic == 2:
        theme = b'Tecnologia'
        palabras = [
            'computadora', 'software', 'hardware', 'programacion', 'lenguajes', 'laptop',
            'teclado', 'procesador', 'memoria', 'monitor', 'graficos', 'intel', 'linux',
            'windows', 'camara', 'sistemas', 'informatica', 'computacion', 'electronica',
            'matematicas', 'ciencias', 'programa', 'codigo', 'ejecutable', 'compilación',
            'interfaz', 'frontend', 'backend', 'desarrollo', 'databases', 'celular', 'telefono',
            'audifonos', 'inalambrico', 'alambrico', 'videojuegos', 'servidor', 'redes',
            'automatico', 'robotica', 'circuitos'
        ]
        while matriz.libres:
            palabra = palabras[random.randint(0, len(palabras) - 1)]
            if verify_word(palabra):
                palabras.remove(palabra)
            else:
                largo = len(palabra)
                matriz.put(palabra)
    elif topic == 3:
        theme = b'Capitales del mundo'
        palabras = [
            'paris', 'madrid', 'lisboa', 'tokio', 'camberra', 'tallin', 'ottawa', 'brasilia',
            'managua', 'caracas', 'amsterdam', 'bruselas', 'helsinki', 'berlin', 'pekin',
            'montevideo', 'belmopan', 'sarajevo', 'praga', 'santiago', 'bogota', 'seul',
            'quito', 'atenas', 'budapest', 'jerusalen', 'roma', 'beirut', 'luxemburgo',
            'mexico', 'panama', 'lisboa', 'londres', 'dakar', 'damasco', 'estocolmo',
            'tunez', 'vaticano', 'lusaka', 'andorra', 'argel', 'viena', 'sofia', 'pionyang'
            'zagreb', 'copenhague', 'bratislavia'
        ]
        while matriz.libres:
            palabra = palabras[random.randint(0, len(palabras) - 1)]
            if verify_word(palabra):
                palabras.remove(palabra)
            else:
                largo = len(palabra)
                matriz.put(palabra)

    return theme, str(matriz), matriz.palabras

# Creando el socket TCP/IP (IPv4)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlace de socket y puerto
server_address = ('localhost', 3000)
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen()

while True:
    # Esperando conexion
    print('\nEsperando para conectarse...')
    connection, client_address = sock.accept()
    try:
        print('concexion desde', client_address)
        data = connection.recv(1)

        # Generar sopa de letras y enviar
        topic, tablero, palabras = start_game()
        print('Solucionario...')
        for key in palabras:
            print('    ', key, ">>", palabras[key])
        connection.sendall(topic)
        connection.sendall(bytes(tablero, encoding='utf-8'))
        connection.sendall(json.dumps(palabras).encode())

        end = connection.recv(32)
        # registrar puntaje
        f = open('winners.txt', 'a')
        f.write('Jugador >>> ' + str(client_address))
        f.write('\n' + 'Puntaje >>> ' + str(end.decode()))
        f.write('\n' + 'Topic >>> ' + topic.decode())
        f.write('\n' + 'Numero palabras >>> ' + str(len(palabras)))
        f.write('\n' + 'Fecha >>> ' + str(datetime.now()) + '\n\n')
        f.close()

        print('Registro de datos de puntaje finales...')

    finally:
        # Cerrando conexion
        connection.close()
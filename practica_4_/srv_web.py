import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def responseThread():
    while True:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        print(request)

        # Parse HTTP headers
        headers = request.split('\n')
        filename = headers[0].split()[1]

        if '?' in filename:
            data = filename.split('?')[1].split('&')
            html = '''
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link rel="stylesheet" href="style.css">
                        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
                        <title>HACKER WEBPAGE | GET RECV</title>
                    </head>
                    <body>
                        <div class="form-data">
                            <h1>Data GET</h1>
                            <div class="data">
                                ''' + data[0] + ''' </br>
                                ''' + data[1] + ''' </br>
                                ''' + data[2] + '''
                            </div>
                        </div>
                    </body>
                    </html>'''
            response = b'HTTP/1.0 200 OK\n\n' + html.encode()
        elif headers[0].startswith('POST'):
            data = headers[-1].split('&')
            html = '''
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link rel="stylesheet" href="style.css">
                        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
                        <title>HACKER WEBPAGE | POST RECV</title>
                    </head>
                    <body>
                        <div class="form-data">
                            <h1>Data POST</h1>
                            <div class="data">
                                ''' + data[0] + ''' </br>
                                ''' + data[1] + ''' </br>
                                ''' + data[2] + '''
                            </div>
                        </div>
                    </body>
                    </html>'''
            with open(server_folder + 'post', 'wb') as fin:
                fin.write(html.encode())
            with open(server_folder + 'post', 'rb') as fin:
                content = fin.read()
            response = b'HTTP/1.0 200 OK\n\n' + content
        elif headers[0].startswith('PUT'):
            data = headers[-1]
            if not data:
                open(server_folder+filename, "w").close()
                response = b'HTTP/1.0 201\n\n'
            else:
                with open(server_folder + filename, 'w') as fin:
                    fin.write(data)
                response = b'HTTP/1.0 201\n\n'
        else:
            # Get the content of the file
            if filename == '/':
                filename = '/index.html'
            try:
                with open(server_folder + filename, 'rb') as fin:
                    content = fin.read()
                # fin = open(server_folder + filename, "rb")
                # content = fin.read()
                # fin.close()
                if headers[0].startswith('HEAD'):
                    date = 'Date: ' + str(datetime.now())
                    c_lengh = 'Content-Length: ' + str(len(content))
                    if filename.endswith('html'):
                        c_type = 'Content-Type: text/html'
                    elif filename.endswith('png'):
                        c_type = 'Content-Type: image/png'
                    elif filename.endswith('jpg'):
                        c_type = 'Content-Type: image/jpg'
                    elif filename.endswith('pdf'):
                        c_type = 'Content-Type: application/pdf'
                    else:
                        c_type = 'text/plain'
                    response = b'HTTP/1.0 200 OK\nServer: Servidor/1.0\n'+date.encode()+b'\n'+ c_lengh.encode()+b'\n'+c_type.encode()+b'\n\n'
                else:
                    response = b'HTTP/1.0 200 OK\n\n' + content

            except FileNotFoundError:
                html = '''
                        <!DOCTYPE html>
                        <html lang="es">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <link rel="stylesheet" href="style.css">
                            <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
                            <title>HACKER WEBPAGE | POST RECV</title>
                        </head>
                        <body>
                            <div class="form-data">
                                <h1>ERROR 404</h1>
                                <div class="data">
                                    File not found. The worst hacker in the history...
                                </div>
                            </div>
                        </body>
                        </html>'''
                response = b'HTTP/1.0 404 NOT FOUND\n\n' + html.encode()

        # Send HTTP response
        client_connection.sendall(response)
        # client_connection.close()


if __name__ == '__main__':
    # Define socket host and port
    SERVER_HOST = 'localhost'
    SERVER_PORT = 8000

    # Define main folder to HTTP server
    server_folder = 'c:/Users/alan_/PycharmProjects/pythonProject3/practica_4_/HTTPserver'

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening in {} on port {} ...\n\n'.format(SERVER_HOST, SERVER_PORT))
    # responseThread()
    executor = ThreadPoolExecutor(max_workers=10)
    executor.submit(responseThread)

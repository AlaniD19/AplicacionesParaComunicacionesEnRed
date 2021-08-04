import Pyro4
import os
import base64

folder = 'clt_download'

if __name__ == "__main__":
    nameserver = Pyro4.locateNS()
    uri = nameserver.lookup("obj")
    file = Pyro4.Proxy(uri)
    # file = Pyro4.resolve("PYRONAME:Server")
    os.chdir(folder)
    while True:
        archive = input('Khe harchivo descargamos crack >>> ')
        items = file.search(str(archive))
        # print('%s Coincidencias encontradas' % len(items))
        if len(items) == 1:
            data = file.download(archive)
            open(archive, 'wb').write(base64.b64decode(data['data']))
            print('\n[+] Harchibo listo... \n')
        else:
            md5 = []
            for i in range(len(items)):
                md5.append(items.count(i))
            for i in range(len(md5)):
                print('Archivo %s encontrado en %s servidores...' % i % md5[i])

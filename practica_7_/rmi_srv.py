import os
import Pyro4
import pathlib
import hashlib

folder = 'srv_1'


@Pyro4.expose
class Server(object):
    def search(self, file):
        hashes = []
        directory = self.path(folder)
        for i in directory:
            if i == file:
                hashes.append(self.getmd5file(file))
        self.count = str(len(hashes)) + ' Coincidencias encontradas...'
        print('%s Coincidencias encontradas' %len(hashes))
        return hashes


    def download(self, file):
        return open(folder+'/'+file, 'rb').read()

    def path(self, folder):
        directorio = pathlib.Path(folder)
        data = []
        for fichero in directorio.iterdir():
            if fichero.is_file():
                data.append(fichero.name)
            else:
                continue
        return data

    def getmd5file(self, file):
        try:
            hashmd5 = hashlib.md5()
            with open(file, "rb") as f:
                for block in iter(lambda: f.read(4096), b""):
                    hashmd5.update(block)
            return hashmd5.hexdigest()
        except Exception as e:
            print("Error: %s" % e)
            return ""
        except:
            print("Error desconocido")
            return ""


if __name__ == '__main__':
    daemon = Pyro4.Daemon()
    uri = daemon.register(Server)
    nameservers = Pyro4.locateNS()
    nameservers.register('obj', uri)
    print("uri=", uri)
    daemon.requestLoop()

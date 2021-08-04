from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import os

local = os.getcwd()
url = 'http://148.204.58.221/axel/aplicaciones/'
domain = 'http://148.204.58.221'


def replace_path(filename):
    with open(filename, 'r') as f:
        content = f.read()
        content = content.replace("src=\"/", "src=\"")
        content = content.replace("href=\"/axel/aplicaciones", "href=\"../index.html")
    with open(filename, 'w+') as f:
        f.write(content)


def dowloader(path):
    if path:
        if str(path[0]).endswith('/'):
            for i in path:
                url_dir = url + str(i)
                dir = requests.get(url_dir, allow_redirects=True)
                try:
                    os.mkdir(str(i).replace('/', ''))
                    print('[+] Directory created / ' + i)
                    os.chdir(str(i).replace('/', ''))
                except EOFError:
                    continue
                # if not os.path.exists(i.split('/')[1]):
                #     os.mkdir(str(i).replace('/', ''))
                #     os.chdir(str(i).replace('/', ''))
                open('index.html', 'wb').write(dir.content)
                print('[+] File downloaded / ' + i)
                replace_path('index.html')
                link_dir, file_dir = links_files(dir)
                for i in link_dir:
                    if i in path:
                        del[i]
                for i in file_dir:
                    if i in path:
                        del[i]
                dowloader(file_dir)
                dowloader(link_dir)
                os.chdir('..')
                if os.getcwd() == local:
                    break
        else:
            for i in path:
                if str(i).startswith('/'):
                    if not os.path.exists(i.split('/')[1]):
                        os.mkdir(i.split('/')[1])
                        print('[+] Directory created / ' + i)
                        os.chdir(i.split('/')[1])
                    else:
                        os.chdir(i.split('/')[1])
                    url_file = domain + i
                    file = requests.get(url_file)
                    filename = str(i).split('/')[-1]
                    if '.' in filename:
                        open(filename, 'wb').write(file.content)
                        print('[+] File downloaded / ' + i)
                    else:
                        filename = filename + '.zip'
                    os.chdir('..')
                    if os.getcwd() == local:
                        break
                else:
                    url_file = url + str(i)
                    file = requests.get(url_file)
                    filename = str(i).split('/')[-1]
                    if '.' in filename:
                        open(filename, 'wb').write(file.content)
                        print('[+] File downloaded / ' + i)
                    else:
                        filename = filename + '.zip'
    else:
        pass


def links_files(html):
    link = []
    file = []
    soup = BeautifulSoup(html.content, "html.parser")
    tags = soup('a')
    for tag in tags:
        if str(tag.get('href')).endswith('/'):
            link.append(tag.get('href'))
        elif str(tag.get('href')).startswith('?'):
            pass
        else:
            file.append(tag.get('href'))
    tags = soup('img') + soup('link') + soup('script')
    for tag in tags:
        file.append(tag.get('src'))
    print('[-] Links and directories getting')
    return link, file


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    myfile = requests.get(url, allow_redirects=True)
    os.mkdir(domain.split('/')[-1])
    os.chdir(domain.split('/')[-1])
    open('index.html', 'wb').write(myfile.content)
    print('[+] Index downloaded')
    replace_path('index.html')
    print('[/] HTML reformated / linked')
    link, file = links_files(myfile)

    executor.submit(dowloader, file)
    executor.submit(dowloader, link)
    # dowloader(file)
    # dowloader(link)
import os
import urllib.request
import zipfile

def directory_verify(directory):
    if os.path.isdir(directory):
        return True
    else: 
        return False

def create_dir(directory):
    os.mkdir(directory)

def download_glassfish4(directory, url):
    dir_download = directory
    file_download = f'{dir_download}\\glassfish-4.0.zip'
    urllib.request.urlretrieve(url, f'{file_download}')

def descompact_zip(filepath, directory):
    zip_file = zipfile.ZipFile(f'{filepath}')
    zip_file.extractall(directory)

directory = r'C:\\glassfish_teste'
url = 'http://download.oracle.com/glassfish/4.0/release/glassfish-4.0.zip'
download_dir = f'{directory}\\download'
descompact_file = f'{download_dir}\\glassfish-4.0.zip'

print('---')
print(f'Diretório de instalação: {directory}')
print(f'URL de download: {url}')
print(f'Diretório de download: {download_dir}')
print(f'Caminho do arquivo a ser descompactado: {descompact_file}')
print('---')

if directory_verify(directory) == False:
    create_dir(directory)
    create_dir(download_dir)
    download_glassfish4(download_dir, url)
    descompact_zip(descompact_file, directory)
else:
    print('Diretório já existe ou já possui dados.')


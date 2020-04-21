import os
import urllib.request
import zipfile
import subprocess
from random import randint


def random_int() -> int:
    return randint(1, 99)


def install_ID() -> str:
    install_ID = install_ID()
    while os.path.isdir(f'C:\\glassish{install_ID}'):
        install_ID = install_ID()
    return  str(install_ID)
    

def create_dir(path: str):
    try:
        os.mkdir(path)
        return True
    except Exception as err:
        print('Problem with creating directory: ', str(err))
        

def download_glassfish(path: str, url: str):
    try:
        urllib.request.urlretrieve(url, f'{path}\\glassfish-4.0.zip')
    except Exception as err:
        print('Problem with download Glassfish: ', str(err))


def descompact_zip(file_path: str, dest_path: str):
    zip_file = zipfile.ZipFile(f'{file_path}')
    try:
        zip_file.extractall(dest_path)
    except Exception as err:
        print('Error unzipping Glassfish: ', str(err))


def glassfish_create_service(asadmin_dir):
    try:
        subprocess.run([asadmin_dir, 'create-service --name domain1'], capture_output=True)
    except Excption as err:
        print('Error creating glassfish service: ', str(err))


#install_path = r'C:\\glassfish_1'
install_ID = install_ID()
install_path = f'C:\\glassfish{install_ID}'
url = 'http://download.oracle.com/glassfish/4.0/release/glassfish-4.0.zip'
download_dir = f'{install_path}\\download'
descompact_file = f'{download_dir}\\glassfish-4.0.zip'
bin_dir = f'{install_path}\\glassfish4\\bin\\asadmin.bat'
line = '=' * 30

print(line)
print(f'Install directory: {install_path}.')
print(f'Download URL: {url}.')
print(f'Download path: {download_dir}.')
print(f'Installation ID: {install_ID}.')
print(line)

print('Criando diretório para instalação...')
create_dir(install_path)
if os.path.isdir(install_path):
    print(f'Diretório criado com sucesso:{install_path}...')
    create_dir(download_dir)
    print(f'Diretório para download criado: {download_dir}...')
    download_glassfish4(download_dir, url)
    print(f'Download realizado: {download_dir}...')
    descompact_zip(descompact_file, directory)
    print(f'Zip descompactado: {descompact_file}...')
    print(f'Criando serviço do Windows: ')
    glassfish_create_service(bin_dir)
else:
    print('Installation Error.')
print('Fineshed!')

#https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
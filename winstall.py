import os
import urllib.request
import zipfile
import subprocess
from random import randint


def random_int() -> int:
    return randint(1, 99)


def install_ID() -> str:
    install_ID = random_int()
    while os.path.isdir(f'C:\\glassish{install_ID}'):
        install_ID = install_ID()
    return  str(install_ID)
    

def create_dir(path: str) -> bool:
    try:
        os.mkdir(path)
        return True
    except Exception as err:
        print('Problem with creating directory: ', str(err))
        

def download_glassfish(path: str, url: str) -> None:
    try:
        urllib.request.urlretrieve(url, f'{path}\\glassfish-4.0.zip')
    except Exception as err:
        print('Problem with download Glassfish: ', str(err))


def descompact_zip(file_path: str, dest_path: str) -> None:
    zip_file = zipfile.ZipFile(f'{file_path}')
    try:
        zip_file.extractall(dest_path)
    except Exception as err:
        print('Error unzipping Glassfish: ', str(err))


def glassfish_create_service(asadmin_dir: str, service_name: str) -> None:
    subprocess.run([asadmin_dir, service_name], capture_output=True)


#install_path = r'C:\\glassfish_1'
install_ID = install_ID()
service_name = f'create-service --name Glassfish Install ID {install_ID}'
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
    print('Iniciando Download...')
    download_glassfish(download_dir, url)
    print(f'Download finalizado: {download_dir}...')
    descompact_zip(descompact_file, install_path)
    print(f'Zip descompactado: {descompact_file}...')
    print(f'Criando serviço do Windows: ')
    print(f'Dir: {bin_dir}.')
    print(bin_dir)
    glassfish_create_service(bin_dir, service_name)
else:
    print('Installation Error.')
print('Fineshed!')

#https://gist.github.com/vladignatyev/06860ec2040cb497f0f3

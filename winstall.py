import os
import urllib.request
import zipfile
import subprocess

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

def glassfish_create_service(bin_dir):
    subprocess.run([bin_dir, 'create-service --name domain1'], capture_output=True)

directory = r'C:\\glassfish_teste'
url = 'http://download.oracle.com/glassfish/4.0/release/glassfish-4.0.zip'
download_dir = f'{directory}\\download'
descompact_file = f'{download_dir}\\glassfish-4.0.zip'
bin_dir = f'{directory}\\glassfish4\\bin\\asadmin.bat'

print('---')
print(f'Diretório de instalação: {directory}')
print(f'URL de download: {url}')
print(f'Diretório de download: {download_dir}')
print(f'Caminho do arquivo a ser descompactado: {descompact_file}')
print(f'Caminho do diretório bin: {bin_dir}')
print('---' * 10)

print('Verificando se diretório existe.' + '\n' + '---' * 10)
if directory_verify(directory) == False:
    print('Diretório não existe, prosseguindo.' + '\n' + '---' * 10)
    create_dir(directory)
    print(f'Diretório criado: {directory}, prosseguindo.' + '\n' + '---' * 10)
    create_dir(download_dir)
    print(f'Diretório para download criado: {download_dir}, prosseguindo.' + '\n' + '---' * 10)
    download_glassfish4(download_dir, url)
    print(f'Download realizado: {download_dir}, prosseguindo.' + '\n' + '---' * 10)
    descompact_zip(descompact_file, directory)
    print(f'Zip descompactado: {descompact_file}, prosseguindo.' + '\n' + '---' * 10)
    print(f'Criando serviço do Windows: ')
    glassfish_create_service(bin_dir)
    print('---' * 10)
else:
    print('Diretório já existe ou já possui dados.')

print('Finalizado!')
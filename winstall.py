import os
import urllib.request
import zipfile

def directory_verify(directory):
    if os.path.isdir(directory):
        dir_empty = os.listdir(directory)
        if len(dir_empty) == 0:
            return True
        else:
            return False
    else:
        return False

def crate_install_dir(directory):
    os.mkdir(directory)

def download_glassfish4(directory, url):
    dir_download = r'{directory}\\download'
    os.mkdir(dir_download)
    file = f'{dir_download}\\glassfish-4.0.zip'
    urllib.request.urlretrieve(url, f'{file}')
    zip_file = zipfile.ZipFile(f'{file}')
    zip_file.extractall(directory)


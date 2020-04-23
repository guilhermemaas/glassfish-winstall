import os
import urllib.request
import zipfile
import subprocess
from random import randint
import socket
import shutil
from print_g4wi import print_g4wi
from time import sleep


def tcp_port_check(ip: str, port: int) -> bool:
    """Checks if a TCP port is in use/open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, int(port)))
        sock.shutdown(2)
        return True
    except:
        return False


def java_check() -> bool:
    """Checks if Java 7 or 8 is installed."""
    version_string = 'java version"1.'
    java_version = subprocess.check_output('java -version', shell=True)
    if 'f{version_string}7' or 'f{version_string}8' in java_version:
        return True
    else:
        return False


def random_int() -> int:
    """Return a random int."""
    return randint(1, 99)


def install_ID() -> str:
    """Checks if installation dir exists
    for return a new installation ID."""
    id = random_int()
    while os.path.isdir(f'C:\\glassish{id}'):
        id = random_int()
    return str(id)


def create_dir(path: str) -> bool:
    """Create a new dir for installation"""
    try:
        os.mkdir(path)
        return True
    except Exception as err:
        print('Problem with creating directory: ', str(err))


def remove_dir(path: str) -> None:
    """Remove directory."""
    try:
        shutil.rmtree(path)
    except Exception as err:
        print('Error to remove directory.', str(err))


def download_glassfish(path: str, url: str) -> None:
    """Download GlassFish from Oracle official link."""
    try:
        urllib.request.urlretrieve(url, f'{path}\\glassfish-4.0.zip')
    except Exception as err:
        print('Problem with download Glassfish: ', str(err))


def descompact_zip(file_path: str, dest_path: str) -> None:
    """Descompact the GlassFish .zip file."""
    zip_file = zipfile.ZipFile(f'{file_path}')
    try:
        zip_file.extractall(dest_path)
    except Exception as err:
        print('Error unzipping Glassfish: ', str(err))


def glassfish_create_service(asadmin_dir: str, asadmin_params: str) -> None:
    """Create GlassFish Windows Service(services.msc)."""
    subprocess.call(rf'{asadmin_dir} {asadmin_params}', shell=True)


def rename_windows_service_display(install_id: str) -> None:
    """Changes the name of the service displayed in services.msc."""
    print(f'sc config GlassFish_{install_id} DisplayName = "GlassFish ID_{install_id}"')
    subprocess.call(f'sc config GlassFish_{install_id} DisplayName= "GlassFish_ID_{install_id}"', shell=True)


def print_line() -> str:
    print('=' * 100)


#Preparing variables to install
install_ID = install_ID()
asadmin_params = f'create-service --name Glassfish_{install_ID}'
install_path = f'C:\\glassfish{install_ID}'
url = 'http://download.oracle.com/glassfish/4.0/release/glassfish-4.0.zip'
download_dir = f'{install_path}\\download'
descompact_file = f'{download_dir}\\glassfish-4.0.zip'
asadmin_dir = f'{install_path}\\glassfish4\\bin\\asadmin.bat'
tcp_port = 4848
ip = '127.0.0.1'
print_g4wi()
sleep(1)
print_line()

print(f'Install directory: {install_path}.')
print(f'Download URL: {url}.')
print(f'Download path: {download_dir}.')
print(f'Installation ID: {install_ID}.')
sleep(1)
print_line()

#Runing functions:
def main() -> None:
    create_dir(install_path)
    if os.path.isdir(install_path) == True:
        print('Checking if Java 1.8 or 1.7 is installed...')
        if java_check():
            print(f'Verifying if port {tcp_port} is in use on {ip}...')
            if tcp_port_check(ip, tcp_port) == False:
                print('TCP port is not in use... OK')
                print('Java version... OK')
                print(f'Directory created sucessfuly:{install_path}...')
                print('Creating download directory...')
                create_dir(download_dir)
                print(f'Download directory created sucessfuly: {download_dir}...')
                print('Starting GlassFish4 download...')
                download_glassfish(download_dir, url)
                print(f'Downloaded in: {download_dir}...\n Unpacking .zip...')
                descompact_zip(descompact_file, install_path)
                print(f'.zip unpacked: {descompact_file}...')
                print(f'Creating Windows Service... ')
                glassfish_create_service(asadmin_dir, asadmin_params)
                print(f'Changing service name to GlassFish ID_{install_ID}.')
                rename_windows_service_display(install_ID)
                print(f'Removing download directory: {download_dir}.')
                remove_dir(download_dir)
                print_line()
                print(f"""
                Finished! Glassfish4 is installed!
                Installation information for deploy:
                    - Glassfish Admin Port: {tcp_port}.
                    - GlassFish HTTP Listner-1: 8080.
                    - Glassfish HTTP Listner-2: 8181.
                    - JVM Options:
                        - XX:MaxPermaSize=192mb.
                        - Xmx512mb.
                """)
            else:
                print_line()
                print(f'TCP port {tcp_port} is not avaible in {ip}. Verify if any program or older Glassfish is using.')
        else:
            print_line()
            print('Java not installed correctly. Reinstall or check JAVA_HOME environment variable.')
    else:
        print_line()
        print('Installation Error.')
    print_line()

if __name__ == "__main__":
    main()

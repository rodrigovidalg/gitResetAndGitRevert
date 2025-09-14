import sys
from colorama import init, Fore
init(autoreset=True)

def saludar(nombre):
    print(Fore.GREEN + f'Hola, {nombre}!')

if len(sys.argv) > 1 and sys.argv[1]:
    saludar(sys.argv[1])
else:
    print(Fore.RED + 'Error: No se proporcionó un nombre para saludar.')

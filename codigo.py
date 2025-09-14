import sys

def saludar(nombre):
    print(f'Hola, {nombre}!')

if len(sys.argv) > 1 and sys.argv[1]:
    saludar(sys.argv[1])
else:
    print('Error: No se proporcionó un nombre para saludar.')

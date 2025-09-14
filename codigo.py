import sys

def saludar(nombre):
    print(f'Hola, {nombre}!')

if len(sys.argv) > 1:
    saludar(sys.argv[1])
else:
    saludar('mundo')

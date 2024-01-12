# %% Librerías
import random as rnd

# %% Presentación del juego
nombre = input(f'¡HOLA JUGEMOS!\n\n¿Como se llamas?\n')
print(
    f'''\nBueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo
ocho (8) intentos para adivinar cuál crees que es el número.\n'''
)

# %% Desarrollo del juego
numero_pc = rnd.randint(0,100)

for intento in range(1,9):
  print(f'\033[1mIntento numero: {intento}/8. \033[0m')
  numero_usuario = int(input('Ingresa un numero dentro del intervalo [0,100].\n'))

  if (numero_usuario < 0) or (numero_usuario >100):
    print(f'Valor ingresado fuera de rango.\n{"-"*40}\n\n')
  elif numero_usuario < numero_pc:
    print(f'Tu numero es \033[1m MENOR \033[0m que el que pensé.\n{"-"*40}',end='\n\n')
  elif numero_usuario > numero_pc:
    print(f'Tu numero es \033[1m MAYOR \033[0m que el que pensé.\n{"-"*40}',end='\n\n')
  elif numero_usuario == numero_pc:
    print(f'\n\033[1m¡FELICITACIONES {nombre.upper()}, GANASTE! \033[0m\nGanaste en el intento numero {intento}.')
    break

if numero_usuario != numero_pc:
  print(f'\033[1mFIN DEL JUEGO \033[0m\nEl numero secreto era: {numero_pc}')
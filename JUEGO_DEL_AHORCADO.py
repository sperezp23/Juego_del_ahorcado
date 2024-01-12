# %% JUEGO DEL AHORCADO

# Librerías e importaciones
from random import choice # Escoje un elemento al azar de un arreglo
from string import ascii_lowercase # String con el alfabeto
from IPython.core.display import clear_output # Limpia la consola

# Función para el dibujo del ahorcado
def ahorcado(vidas:int)->None:

  '''
  Imprime los diferences estados del ahorcado.
  '''

  match vidas:
    case 6:
      print('''   ___
  |
  |
  |
 _|_\n''')

    case 5:
      print('''   ___
  |   o
  |
  |
 _|_\n''')

    case 4:
      print('''   ___
  |   o
  |   |
  |
 _|_\n''')

    case 3:
      print('''    ___
   |   o
   |  /|
   |
  _|_\n''')

    case 2:
      print('''    ___
   |   o
   |  /|\\
   |
  _|_\n''')

    case 1:
      print('''    ___
   |   o
   |  /|\\
   |  /
  _|_\n''')

    case 0:
      print('''    ___
   |   o
   |  /|\\
   |  / \\
  _|_\n''')

# Función para imprimir los guiones
def imprimir_guiones(guiones:list)->None:
  '''
  Imprime la lista de guiones.
  '''

  for i in guiones:
    print(i, end=' ')

# Declaración de variables
palabras = (
    'hola',
    'casa',
    'perro',
    'python',
    'computador',
    'alambrada',
    'protocolo'
)
emojies = {
    6:'\U0001F603',
    5:'\U0001F928',
    4:'\U0001F605',
    3:'\U0001F643',
    2:'\U0001F915',
    1:'\U0001F976',
    0:'\U0001F480'
}
palabra_secreta = choice(palabras)
guiones = list('_'*len(palabra_secreta))
indices = []
vidas = 6
letra_valida = False

# Imprimir el mensaje de bienvenida
print(f'\033[1mJUEGO DEL AHORCADO\033[\n\nTe quedan [{vidas}/6] {emojies[vidas]} vidas\n')
ahorcado(vidas)

# Imprimir los primeros guiones
imprimir_guiones(guiones)

# Ciclo While para mantener al juego corriendo mientras el jugados tenga vidas
while vidas > 0:

  # Verificar que la palabra ya esté completa
  if '_' not in guiones:
    print('\n\n\U0001F92F ¡Ganaste! \U0001F973')
    break

  # Pide la entrada al usuario, si no es valida, la vuelve a pedir
  while not letra_valida:
    letra_usiario = input('\n\nIngresa una letra\n').lower()

    # Si la letra está en el abecedario
    if letra_usiario in ascii_lowercase:
      clear_output()
      letra_valida = True

    else:
      print('Caracter invalido \U0001F635')

  # Verifica que la letra ingresada esté en la palabra a adivinar
  if letra_usiario in palabra_secreta:

    # Imprimir numero de vidas y el ahorcado
    print(f'\nTe quedan [{vidas}/6] vidas {emojies[vidas]}\n')
    ahorcado(vidas)

    # Buscar las letras repetidas en la palabra secreta
    for j in range(len(palabra_secreta)):

      # Cambiar los guiones por letras
      if palabra_secreta[j] == letra_usiario:
        guiones[j] = letra_usiario

      # Imprimir los guiones aprovechando este ciclo
      print(guiones[j], end=' ')

  # Si la letra ingresada no se halla en la palabra secreta
  else:
    vidas -= 1
    ahorcado(vidas)
    print(f'\nLetra equivocada \U0001F616\nTe quedan [{vidas}/6] {emojies[vidas]} vidas\n')

    #Imprimir los guiones otra vez
    imprimir_guiones(guiones)

  letra_valida = False

# Si ya no quedan vidas, imrpima los mensajes respectivos
if vidas == 0:
  print(f'\n\nFin del juego\tPerdiste \U0001F62D')
  print('''    ___
   |  \033[4m o \033[
   |  /|\\
   |  / \\
  _|_''')
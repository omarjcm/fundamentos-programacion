'''
Basado en el ejercicio de ejemplo mostrado en el Curso de Platzi: "Curso de Python".
'''
import random

IMAGENES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
    |   |
   / \\  |
        =========''', '''
''']

PALABRAS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

NUM_INTENTOS = 7

def palabra_aleatoria():
    ''' randint recibe como primer parámetro el valor inicial incluido 
        y el valor final incluído
    ''' 
    indice = random.randint( 0, len( PALABRAS ) - 1 )
    return PALABRAS[ indice ]

def run():
    palabra = palabra_aleatoria()
    palabra_oculta = [ '-' ] * len( palabra )
    intento = 0

    while True:
        print( IMAGENES[ intento ] )
        print( '' )

        if intento == NUM_INTENTOS:
            print()
            print( '¡Perdiste! La palabra correcta era {}'.format( palabra ) )
            break

        print( palabra_oculta )
        print( '--- * --- * --- * --- * --- * --- ' )

        letra_actual = input( 'Escoge una letra: ' )

        palabra_indices = []
        for i in range( len(palabra) ):
            if ( palabra[i] == letra_actual ):
                palabra_indices.append( i )
            
        if (len(palabra_indices) == 0):
            # Cuando no se encuentra la letra ingresada en la palabra aleatoria
            intento += 1
        else:
            for i in palabra_indices:
                palabra_oculta[i] = letra_actual
        
        try:
            palabra_oculta.index( '-' )
        except ValueError:
            print()
            print( '¡Felicitaciones! Ganaste. La palabra es: {}'.format( palabra ) )
            break

        

if _name_ == '_main_':
    print( "B I E N V E N I D O   A   A H O R C A D O S" )
    run()
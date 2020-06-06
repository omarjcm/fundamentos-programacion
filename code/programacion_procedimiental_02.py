def rombo_arriba():
    print( "   /\\   " )
    print( "  /  \\  " )
    print( " /    \\ " )

def rombo_abajo():
    print( " \\    / " )
    print( "  \\  /  " )
    print( "   \\/   " )

def cuadrado():
    print( "+------+ " )
    print( "|      | " )
    print( "|      | " )
    print( "+------+ " )

def grafica():
    rombo_arriba()
    rombo_abajo()
    print( "         " )
    rombo_abajo()
    rombo_arriba()
    print( "         " )
    rombo_arriba()
    cuadrado()
    print( "| ECU  | " )
    print( "|      | " )
    cuadrado()
    rombo_arriba()

grafica()
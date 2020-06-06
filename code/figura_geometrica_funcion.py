def arriba():
    print( "  _______    " )
    print( " /       \\  " )
    print( "/         \\ " )

def abajo():
    print( "\\         / " )
    print( " \\_______/  " )

def stop():
    print( "|  STOP   |  " )

def grafica():
    arriba()
    abajo()
    abajo()
    print( " +-------+   " )
    print( "             " )
    arriba()
    abajo()
    print( "             " )
    arriba()
    print( "+---------+  " )

grafica()

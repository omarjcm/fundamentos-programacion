def menu_principal():
  print( " =================================== " )
  print( " CALCULADORA                         " )
  print( " =================================== " )
  print( " Menú Principal: " )
  print( " [1].- Sumar " )
  print( " [2].- Restar " )
  print( " [3].- Multiplicar " )
  print( " [4].- Dividir " )
  print( " [5].- Salir " )
  opcion = input("Elegir una opción (1-5): ");
  return int( opcion )

def calculadora():
  centinela = True
  while( centinela ):
    opcion = menu_principal()

    # Aquí va todo el código

    if opcion == 5:
      centinela = False
      print( "Gracias por utilizar nuestra calculadora" )

calculadora()

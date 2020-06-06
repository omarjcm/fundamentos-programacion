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
  opcion = input("Elegir una opción (1-5): ")
  return int( opcion )

def titulo_operacion( titulo ):
  print( "\n\n =================================== " )
  print( " CALCULADORA - " + titulo )
  print( " =================================== " )

def resultado( tipo_operacion, valor ):
  print( " =================================== " )
  print( "El resultado de la " + tipo_operacion + " es: " + str( valor ) )
  print( " =================================== \n\n" )


def sumar():
  titulo_operacion( "SUMAR" )
  num1_ = input("Ingresar primer número: ")
  num1 = int( num1_ )
  num2_ = input("Ingresar segundo número: ")
  num2 = int( num2_ )
  resultado( "suma", num1 + num2 )
  
def restar():
  titulo_operacion( "RESTAR" )
  num1_ = input("Ingresar primer número: ")
  num1 = int( num1_ )
  num2_ = input("Ingresar segundo número: ")
  num2 = int( num2_ )
  resultado( "resta", num1 - num2 )

def multiplicar():
  titulo_operacion( "MULTIPLICAR" )
  num1_ = input("Ingresar primer número: ")
  num1 = int( num1_ )
  num2_ = input("Ingresar segundo número: ")
  num2 = int( num2_ )
  resultado( "multiplicación", num1 * num2 )

def dividir():
  titulo_operacion( "DIVIDIR" )
  num1_ = input("Ingresar primer número: ")
  num1 = int( num1_ )
  num2_ = input("Ingresar segundo número: ")
  num2 = int( num2_ )
  if (num2 == 0):
    print( "No se puede dividir para cero." )
  else:
    resultado( "división", num1 / num2 )

def calculadora():
  centinela = True
  while( centinela ):
    opcion = menu_principal()

    if opcion == 1:
      sumar()
    elif opcion == 2:
      restar()
    elif opcion == 3:
      multiplicar()
    elif opcion == 4:
      dividir()
    elif opcion == 5:
      centinela = False
      print( "Gracias por utilizar nuestra calculadora" )

calculadora()

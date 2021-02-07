# Metodo para encriptar 
def encriptar():
  # Obtenemos mensaje a cifrar desde el usuario
  # llamamos a upper para obtener sólo mayúsculas
  y = input("Mensaje: ").upper()

  # Pedimos al usuario la cantidad de desplazamiento
  x = int(input("Desplazamiento: "))

  # Abecedario a utilizar en el cifrado
  abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"

  # Variable para guardar mensaje cifrado
  cifrado = ""

  # Iteramos por cara letra del mensaje
  for elemento in y:
      # Si la letra está en el abecedario se reemplaza
      if elemento in abc:
          pos_letra = abc.index(elemento)
          # Sumamos para movernos a la derecha del abc teniendo en cuenta el modulo
          nueva_pos = (pos_letra + x) % len(abc)
          cifrado+= abc[nueva_pos]
      else:
          # Si no está en el abecedario sólo añadelo
          cifrado += elemento

  print("Mensaje cifrado: ", cifrado)
  
  def descencriptar():
  # Obtenemos mensaje a cifrar desde el usuario
  # llamamos a upper para obtener sólo mayúsculas
  y = input("Mensaje: ").upper()

  # Pedimos al usuario la cantidad de desplazamiento
  z = int(input("Desplazamiento: "))

  # Abecedario a utilizar en el cifrado
  abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"

  # Variable para guardar mensaje cifrado
  descifrado = ""

  # Iteramos por cara letra del mensaje
  for elemento in y:
      # Si la letra está en el abecedario se reemplaza
      if elemento in abc:
          pos_letra = abc.index(elemento)
          # Sumamos el inverso aditivo para movernos a la izquierda del abc teniendo en cuenta el modulo
          nueva_pos = (pos_letra + (len(abc)-z)) % len(abc)
          descifrado += abc[nueva_pos]
      else:
          # Si no está en el abecedario sólo añadelo
          descifrado += elemento

  print("Mensaje Descifrado: ", descifrado)
  
  
  while True:
  try:
    print("\n\n*******************************************BIENVENIDO********************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("1. Encriptar .\n2. Descencriptar\n3. Salir\n"))
    if opc == 1:
      encriptar()
    elif opc == 2:
      descencriptar()
    elif opc == 3:
      print("Hasta luegpo :)")
      break
    else: 
      print("El valor ingresado no es valido")


  except ValueError:
    print("El valor ingresado no es valido")
  except KeyboardInterrupt:
    print("Ha detenido el programa bruscamente")
  except:
    print("Algo salió mal. Posiblemente no ha ejecutado todas las celdas de código")
  finally:
    print("Fin")
    
    
    
    
    -------------------------------------------------- 2 ------------------------------------------------
    
    # Obtenemos mensaje a cifrar desde el usuario
# llamamos a upper para obtener sólo mayúsculas
y = input("Mensaje: ").upper()

# Pedimos al usuario la cantidad de desplazamiento
x = int(input("Desplazamiento: "))

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"

# Variable para guardar mensaje cifrado
cifrado = ""

# Iteramos por cara letra del mensaje
for elemento in y:
    # Si la letra está en el abecedario se reemplaza
    if elemento in abc:
        pos_letra = abc.index(elemento)
        # Sumamos para movernos a la derecha del abc
        nueva_pos = (pos_letra + x) % len(abc)
        cifrado+= abc[nueva_pos]
    else:
        # Si no está en el abecedario sólo añadelo
        cifrado += elemento

print("Mensaje cifrado: ", cifrado)

# Obtenemos mensaje a cifrar desde el usuario
# llamamos a upper para obtener sólo mayúsculas
y = input("Mensaje: ").upper()

# Pedimos al usuario la cantidad de desplazamiento
z = int(input("Desplazamiento: "))

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Variable para guardar mensaje cifrado
descifrado = ""

# Iteramos por cara letra del mensaje
for elemento in y:
    # Si la letra está en el abecedario se reemplaza
    if elemento in abc:
        pos_letra = abc.index(elemento)
        # Sumamos el inverso aditivo para movernos a la izquierda del abc
        nueva_pos = (pos_letra + (len(abc)-z)) % len(abc)
        descifrado += abc[nueva_pos]
    else: 
        # Si no está en el abecedario sólo añadelo
        descifrado += elemento

print("Mensaje Descifrado: ", descifrado)

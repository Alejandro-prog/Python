import numpy as np
import math as mt
import os

#Clase que modela una Pila para almacenar números enteros
class PilaEnteros:
  #atributos de clase
  pila = [None] * 10
  posicion = -1
  
  #Método que inserta un nuevo elemento en la Pila
  #Parámetro elemento es el nuevo dato para almacenar en la pila
  def push(self, elemento):
    self.posicion += 1
    self.pila[self.posicion] = elemento
    
  #Método que remueve el elemento de la cima
  def pop(self):
    resultado = self.pila[self.posicion]
    self.pila[self.posicion] = None
    self.posicion -= 1
    return resultado
  
  #Método que permite obtener (sin removerlo) el elemento de la cima
  def getTop(self):
    return self.pila[self.posicion]
  
  #Método que retorna la cantidad de elementos almacenados en la pila
  def getNumberOfElements(self):
    return self.posicion + 1
  
  #Método que indica si la pila se encuentra llena
  def isFull(self):
    if self.posicion == 9:
      return True
    else:
      return False

  #Método que indica si la pila se encuentra vacía
  def isEmpty(self):
    if self.posicion == -1:
      return True
    else:
      return False
      
#Clase que modela una Cola para almacenar números reales
class ColaReales:
  #atributos de clase
  cola = []

  #Método que inserta un nuevo elemento en la Cola
  #parámetro elemento es el nuevo dato para almacenar en la cola
  def queue(self, elemento):
    self.cola.insert(0, elemento)
  
  #Método que remueve el primer elemento de la cola
  def dequeue(self):
    return self.cola.pop() 
  
  #Método que permite obtener (sin removerlo) el primer elemento de la cola
  def getFirst(self):
    return self.cola[-1]
  
  #Método que retorna la cantidad de elementos almacenados en la cola
  def getNumberOfElements(self):
    return len(self.cola)
  
  #Método que indica si la cola se encuentra llena
  def isFull(self):
    pass

  #Método que indica si la cola se encuentra vacía
  def isEmpty(self):
    if len(self.cola) == 0:
      return True
    else:
      return False
def subMain2():
  cola = ColaReales()
  while True:
    print("\n\n*******************************************GESTIÓN COLA********************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("1. Agregar un elemento.\n2. Remover primer elemento.\n3. Obtener primer elemento.\n4. Cantidad elementos Cola.\n5. Validar Cola llena.\n6. Validar Cola vacía.\n7. Regresar.\n"))
    if opc == 1:
      if cola.isFull():
        print("La cola está llena")
      else:
        n = float(input("Ingrese el valor a insertar a la Cola\n"))
        cola.queue(n)
        print(n, " fue insertado a la cola")
    elif opc == 2:
      if cola.isEmpty():
        print("La cola está vacía")
      else:
        print("El elemento: ", cola.dequeue(), " fue removido")
    elif opc == 3:
      if cola.isEmpty():
        print("La cola está vacía")
      else:
        print("El primer elemento es: ", cola.getFirst())
    elif opc == 4:
      print("La cola tiene ", cola.getNumberOfElements(), " elementos")
    elif opc == 5:
      if cola.isFull():
        print("La cola está llena")
      else:
        print("La cola aún no está llena")
    elif opc == 6:
      if cola.isEmpty():
        print("La cola está vacía")
      else:
        print("La cola no está vacía")
    elif opc == 7:
      break
      
 def subMain1():
  pila = PilaEnteros()
  while True:
    print("\n\n*******************************************GESTIÓN PILA********************************************\n\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("1. Agregar un elemento.\n2. Remover elemento cima.\n3. Obtener elemento cima.\n4. Cantidad elementos Pila.\n5. Validar Pila llena.\n6. Validar Pila vacía.\n7. Regresar.\n"))
    if opc == 1:
      if pila.isFull():
        print("La pila está llena")
      else:
        n = int(input("Ingrese el valor a insertar en la Pila\n"))
        pila.push(n)
        print(n, " fue insertado a la cola")
    elif opc == 2:
      if pila.isEmpty():
        print("La pila está vacía")
      else:
        print("El elemento: ", pila.pop(), " fue removido")
    elif opc == 3:
      if pila.isEmpty():
        print("La pila está vacía")
      else:
        print("El elemento de la cima es: ", pila.getTop())
    elif opc == 4:
      print("La pila tiene ", pila.getNumberOfElements(), "elementos")
    elif opc == 5:
      if pila.isFull():
        print("La pila está llena")
      else:
        print("La pila aún no está llena")
    elif opc == 6:
      if pila.isEmpty():
        print("La pila está vacía")
      else:
        print("La pila no está vacía")
    elif opc == 7:
      break
      
while True:
  try:
    print("\n\n*******************************************BIENVENIDO********************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("1. Gestionar Pila.\n2. Gestionar Cola.\n3. Finalizar.\n"))
    if opc == 1:
      subMain1()
    elif opc == 2:
      subMain2()
    elif opc == 3:
      print("Hasta la próxima (con voz de loquendo)")
      break

  except ValueError:
    print("El valor ingresado no es valido")
  except KeyboardInterrupt:
    print("No lo detenga así")
  except UnboundLocalError:
    print("Primero debe agregar un elemento")
  except:
    print("Algo salió mal. Posiblemente no ha ejecutado todas las celdas de código")
  finally:
    print("FIN")

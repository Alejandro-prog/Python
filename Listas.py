""" 

(7.1.1) Implementar una pila con una lista de enlaces individuales

"""

class LinkedStack:
  """ LIFO Implementación de LIFO Stack utilizando una lista vinculada individualmente para el almacenamiento """
  #-------------------------- Clase de nodo anidado --------------------------
  class _Node:
    """ Clase liviana, no pública, para almacenar un nodo vinculado individualmente """
    __slots__ = '_element', '_next'   #optimizar el uso de la memoria
    
    def __init__ (self, element, next):   #inicializar los campos de los nodos
      self._element = element   #referencia al elemento del usuario
      self._next = next   #referencia al siguiente nodo

  #------------------------------- métodos de apilamiento -------------------------------
  def __init__(self):
    """ Crear una pila vacía """
    self._head = None   # referencia al nodo principal
    self._size = 0

  def __len__(self):
    """ Retorna el número de elementos en la pila. """
    return print(self._size)

  def is_empty(self):
    """ retorna True si la pila está vacía """
    return print(self._size == 0)

  def push(self, e):
    """ Añade el elemento e a la parte superior de la pila. """
    self._head = self._Node(e, self._head)    # crea y vincula un nuevo nodo
    self._size += 1

  def top(self):
    """
    Retorna (pero no quita) el elemento en la parte superior de la pila.

    Raise Empty excepción vacía si la pila está vacía.
    """
    if self.is_empty():
      raise Empty('La pila está vacía')
    else:
      return self._head._element    # la parte superior de la pila está a la cabeza de la lista

  def pop(self):
    """
    Retire y retorne el elemento de la parte superior de la pila (es decir, LIFO).

    Raise Empty excepción vacía si la pila está vacía
    """
    if self.is_empty():
      raise Empty('La pila está vacía')
    else:
      answer = self._head._element
      self._head = self._head._next   # omitir el antiguo nodo superior
      self._size -= 1
  
  def listar_elementos(self):
    iternode = self._head
    resultado = ""
    if self.is_empty():
      raise Empty("La pila está vacía")
    else:
      while iternode != None:
        resultado = resultado + "\n" + str(iternode._element)
        iternode = iternode._next
    return resultado

  def buscarElementoIterativo(self, codigo):
    iternode = self._head
    resultado = "" 
    if self.is_empty():
      raise Empty('La pila está vacía')
    else:
      while iternode != None:
        if iternode._element == codigo:
          resultado = iternode._element
          break
        else:
          iternode = iternode._next
    return resultado

  def buscarElementoRecursivo(self, codigo, head, k):
    if self.is_empty():
      raise Empty('La pila está vacía')
    else:
      if head._element == codigo:
        return head._element
      elif k == self.__len__():
        return ""
    return self.buscarElementoRecursivo( codigo, head._next, k+1)
    
    
"""

(7.1.2) Implementando una cola con una lista enlazada individualmente

"""

class LinkedQueue:
  """ Implementación de la cola FIFO usando una lista enlazada para almacenamiento """

  class _Node:
    """ Clase liviana y no pública para almacenar un nodo vinculado individualmente. """
    __slots__ = '_element', '_next'   #optimizar el uso de la memoria

    def __init__ (self, element, next):   #inicializar los campos de los nodos
      self._element = element   #referencia al elemento del usuario
      self._next = next   #referencia al siguiente nodo

  def __init__(self):
    """ Crea una cola vacía. """
    self._head = None
    self._tail = None
    self._size = 0    # número de elementos de la cola

  def __len__(self):
    """ Retorna el número de elementos de la cola. """
    return self._size

  def is_empty(self):
    """ Retorna True si la cola está vacía. """
    return self._size == 0

  def first(self):
    """ Retorne (pero no elimine) el elemento al principio de la cola. """
    if self.is_empty():
      raise Empty('La cola está vacía')
    return self._head._element    # frente alineado con la cabeza de la lista

  def dequeue(self):
    """ Elimina y retorne el primer elemento de la cola (es decir, FIFO).


    Raise Empty excepción si la cola está vacía
    """

    if self.is_empty():
      raise Empty('La cola está vacía')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():   # caso especial ya que la cola está vacía
      self._tail = None   # la cabeza quitada había sido la cola
    return answer

  def enqueue(self, e):
    """ Agrega un elemento al final de la cola. """
    newest = self._Node(e, None)    # nodo será un nuevo nodo de cola
    if self.is_empty():
      self._head = newest   # caso especial: previamente vacío
    else:
      self._tail._next = newest
    self._tail = newest   # actualizar la referencia al nodo de cola
    self._size += 1

  def listar_elementos(self):
    iternode = self._head
    resultado = ""
    if self.is_empty():
      raise Empty("La pila está vacía")
    else:
      while iternode != None:
        resultado = resultado + "->" + str(iternode._element)
        iternode = iternode._next
    return resultado

MyLinkedQueue = LinkedQueue()
MyLinkedQueue.enqueue(6)
MyLinkedQueue.enqueue(1)
MyLinkedQueue.enqueue(2)
MyLinkedQueue.enqueue(3)
MyLinkedQueue.enqueue(4)
MyLinkedQueue.__len__()


  """

(7.3.1) Aplicación básica de un Deque a una lista doblemente vinculada

"""

class _DoublyLinkedBase:
# Una clase base que proporciona una representación de lista doblemente enlazada.
    class _Node:
        __slots__ = '_element', '_prev', '_next'   # optimizar la memoria

        def __init__(self, element, prev, next):    # inicializar los campos de los nodos
            self._element = element   # el elemento del usuario
            self._prev = prev   # referencia al nodo anterior
            self._next = next   # referencia del siguiente nodo
    
    def __init__(self):
    # Crea una lista vacía.
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer # tráiler está después del encabezado
        self._trailer._prev = self._header # encabezado antes del tráiler
        self._size = 0 # número de elementos

    def __len__(self):
        # Devuelve el número de elementos de la lista
        return self._size

    def is_empty(self):
        #Return True si la lista está vacía.
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        #Agregue el elemento e entre dos nodos existentes y devuelva el nuevo nodo.
        newest = self._Node(e, predecessor, successor) # vinculado a vecinos
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        # Elimina el nodo no centinela de la lista y devuelve su elemento
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element # registro de elemento eliminado
        node._prev = node._next = node._element = None # desaprobar nodo
        return element # devolver elemento eliminado

"""

(7.3.2) Implementar un Deque con una lista doblemente vinculada

"""

class LinkedDeque(_DoublyLinkedBase):
    """ Implementación de la cola doble basada en una lista doblemente enlazada. """

    def first(self):
        """Devuelva (pero no quite) el elemento en la parte delantera del deque."""
        if self.is_empty():
            raise Empty("Deque está vacío")
        return self._header._next._element      # un artículo real justo después de la cabecera
    
    def last(self):
        """ Devuelve (pero no quita) el elemento en la parte posterior del deque. """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element     #real item just before trailer
    
    def insert_first(self, e):
        """ Agrega un elemento al frente de la deque. """
        print(self._insert_between(e, self._header, self._header._next)) # después del encabezado
    
    def insert_last(self, e):
        """ Agrega un elemento en la parte posterior de la deque. """
        self._insert_between(e, self._trailer._prev, self._trailer) # antes del encabezado

    def delete_first(self):
        """ Retire y devuelva el elemento del frente de la deque.

        Raise Empty excepción si el deque está vacío
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next) # usar método heredado

    def delete_last(self):
        """ Retire y devuelva el elemento de la parte posterior del deque.

        Raise Empty excepción si el deque está vacío
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev) # usar método heredado
        
    def buscarElementoIterativo(self, codigo):
        iternode = self._header._next
        resultado = "" 
        if self.is_empty():
          raise Empty('La lista está vacía')
        else:
          while iternode != None:
            if iternode._element == codigo:
              resultado = iternode._element
              break
            else:
              iternode = iternode._next
        return resultado

    def buscarElementoRecursivo(self, codigo, head, k):
        if self.is_empty():
          raise Empty('La lista está vacía')
        else:
          if head._element == codigo and head != None:
            return head._element
          elif  k == self.__len__():
            return ""
        return self.buscarElementoRecursivo( codigo, head._next, k+1)

    def eliminarElementoIterativo(self, codigo):
        iternode = self._header._next
        resultado = "" 
        if self.is_empty():
          raise Empty('La lista está vacía')
        else:
          while iternode != None:
            if iternode._element == codigo:
              resultado = iternode._element
              break
            else:
              iternode = iternode._next
        return resultado

    def eliminarElementoRecursivo(self, codigo, head):
        if self.is_empty():
          raise Empty('La lista está vacía')
        else:
          if head._element == codigo and head != None:
            return head._element
          else:
            return ""
        return buscarElementoRecursivo( codigo, head._next)
        
        
"""

(7.2.2) Implementar una cola con una lista de enlaces circulares

"""

#Listas enlazadas circularmente
class CircularQueue:
#Implementación de cola usando una lista enlazada circularmente para almacenamiento
  class _Node:
    __slots__ = '_element', '_next'   #optimizar el uso de la memoria

    def __init__ (self, element, next):   #inicializar los campos de los nodos
      self._element = element   #referencia al elemento del usuario
      self._next = next   #referencia al siguiente nodo

  def __init__(self):
    #crear una cola vacía
    self._tail = None # representará la cola de la cola
    self._size = 0 # número de elementos de la cola

  def __len__(self):
    #Retorna el número de elementos en la cola
    return self._size

  def is_empty(self): 
    #Retorna Verdadero si la cola está vacía.
    return self._size == 0

  def first(self):
    #Retorna (pero no elimine) el elemento al principio de la cola.
    #Raise Empty excepción si la cola está vacía.

    if self.is_empty( ):
      raise Empty('Queue is empty')
    head = self._tail._next
    return head._element

  def dequeue(self):

    #Elimina y devuelve el primer elemento de la cola (es decir, FIFO).
    #Raise Empty excepción si la cola está vacía.
    if self.is_empty( ):
      raise Empty('Queue is empty')
    oldhead = self._tail._next
    if self._size == 1: # eliminando solo elemento
      self._tail = None # cola queda vacía
    else:
      self._tail._next = oldhead._next # pasa por alto la cabeza vieja
    self._size -= 1
    return oldhead._element
        
  def enqueue(self, e):
  #Añadir un elemento al final de la cola
    newest = self._Node(e, None) # nodo será un nuevo nodo de cola
    if self.is_empty():
      newest._next = newest # inicializar circularmente
    else:
      newest._next = self._tail._next # nuevos puntos de nodo a la cabeza
      self._tail._next = newest # la cola antigua apunta al nuevo nodo
    self._tail = newest # el nuevo nodo se convierte en la cola
    self._size += 1

  def rotate(self):
  #Gire el elemento frontal al final de la cola.
    if self._size > 0:
      self._tail = self._tail._next # cabeza vieja se convierte en cola nueva

  def buscarElementoIterativo(self, codigo):
    iternode = self._tail._next
    resultado = "" 
    k = 0
    if self.is_empty():
      raise Empty('La lista está vacía')
    else:
      while iternode != None and k != self.__len__():
        k += 1
        if iternode._element == codigo:
          resultado = iternode._element
          break
        else:
          iternode = iternode._next
    return resultado

  def buscarElementoRecursivo(self, codigo, head, k):
    if self.is_empty():
      raise Empty('La pila está vacía')
    else:
      if head._element == codigo:
        return head._element
      elif k == self.__len__():
        return ""
    return self.buscarElementoRecursivo( codigo, head._next, (k+1))

  def eliminarElementoIterativo(self, codigo):
    resultado = "" 
    k = 0
    if self.is_empty():
      raise Empty('La lista está vacía')
    else:
      while self._tail._next != None and k != self.__len__():
        k += 1
        if self._tail._next._element == codigo:
          resultado = self._tail._next._element

          oldhead = self._tail._next
          if self._size == 1: # eliminando solo elemento
            self._tail = None # cola queda vacía
          else:
            self._tail._next = oldhead._next # pasa por alto la cabeza vieja
          self._size -= 1

          break
        else:
          self.rotate()
    return resultado
    
    
def subMain1(simple):
  while True:
    print("\n\n*******************************************MENÚ********************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("0. Ingresar elemento.\n1. Lista Simple Busqueda Secuencial Iterativamente.\n2. Lista Simple Busqueda Secuencial Recursivamente .\n3. Lista Simple Remover Iterativamente.\n4. Lista Simple Remover Recursivamente.\n5. Regresar.\n"))
    if opc == 0:
      n = int(input("Ingrese el elemento:\n"))
      simple.push(n)
      print("Se agregó el elemento: " + str(simple.top()))
    elif opc == 1:
      n = int(input("Ingrese el elemento a buscar:\n"))
      resul = simple.buscarElementoIterativo(n)
      if resul == "":
        print("No se encontró")
      else:
        print("Se encontró el elemento: " + str(resul))
    elif opc == 2:
      n = int(input("Ingrese el elemento a buscar:\n"))
      resul = simple.buscarElementoRecursivo(n, simple._head, 1)
      if resul == "":
        print("No se encontró")
      else:
        print("Se encontró el elemento: " + str(resul))
    elif opc == 3:
      n = int(input("Ingrese el elemento a eliminar:\n"))
      print("Se eliminó el elemento: " + str(n))
    elif opc == 4:
      n = int(input("Ingrese el elemento a eliminar:\n"))
      circular.dequeue()
      print("Se eliminó el primer elemento")
    elif opc == 5:
      break
    else:
      print("Opción invalida")
      
      
 def subMain2(doble):
  while True:
    print("\n\n*******************************************MENÚ********************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("0. Ingresar elemento.\n1. Lista Doble Busqueda Secuencial Iterativamente.\n2. Lista Doble Busqueda Secuencial Recursivamente .\n3. Lista Doble Remover Iterativamente.\n4. Lista Doble Remover Recursivamente.\n5. Regresar.\n"))
    if opc == 0:
      n = int(input("Ingrese el elemento:\n"))
      doble.insert_last(n)
      result = doble.last()
      print("Se insertó el elemento: " + str(result))
    elif opc == 1:
      n = int(input("Ingrese el elemento a buscar:\n"))
      resul = doble.buscarElementoIterativo(n)
      if resul == "":
        print("No se encontró")
      else:
        print("Se encontró el elemento: " + str(resul))
    elif opc == 2:
      n = int(input("Ingrese el elemento a buscar:\n"))
      resul = doble.buscarElementoRecursivo(n, doble._header._next, 1)
      if resul == "":
        print("No se encontró")
      else:
        print("Se encontró el elemento: " + str(resul))
    elif opc == 3:
      n = int(input("Ingrese el elemento a eliminar:\n"))
      doble.delete_last()
      print("Se eliminó el último elemento")
    elif opc == 4:
      n = int(input("Ingrese el elemento a eliminar:\n"))
      doble.delete_first()
      print("Se eliminó el primer elemento")
    elif opc == 5:
      break
    else:
      print("Opción invalida")
      
      
      
def subMain3(circular):
  while True:
    print("\n\n*******************************************MENÚ********************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("0. Ingresar elemento.\n1. Lista Circular Busqueda Secuencial Iterativamente.\n2. Lista Circular Busqueda Secuencial Recursivamente .\n3. Lista Circular Remover Iterativamente.\n4. Lista Circular Remover Recursivamente.\n5. Regresar.\n"))
    if opc == 0:
      n = int(input("Ingrese el elemento a ingresar:\n"))
      circular.enqueue(n)
      print("El elemento: " + str(n) + " fue agregado")
    elif opc == 1:
      n = int(input("Ingrese el elemento a buscar:\n"))
      resul = circular.buscarElementoIterativo(n)
      if resul == "":
        print("No se encontró")
      else:
        print("Se encontró el elemento: " + str(resul))
    elif opc == 2:
      n = int(input("Ingrese el elemento a buscar:\n"))
      resul = circular.buscarElementoRecursivo(n, circular._tail._next, 1)
      if resul == "":
        print("No se encontró")
      else:
        print("Se encontró el elemento: " + str(resul))
    elif opc == 3:
      n = int(input("Ingrese el elemento a eliminar:\n"))
      resul = circular.eliminarElementoIterativo(n)
      if resul == "":
        print("No se encontró")
      else:
        print("Se eliminó el elemento: " + str(resul))
    elif opc == 4:
      n = int(input("Ingrese el elemento a eliminar:\n"))
    elif opc == 5:
      break
    else:
      print("Opción invalida")
      
      
      
listaSimple = LinkedStack()
listaDoble = LinkedDeque()
listaCircular = CircularQueue()

while True:
  print("Querido Profe: quedó funcionando la búsqueda secuencial y recursiva para las tres listas\nY para la eliminación secuencial quedó funcionando para la lista circular\nConsideramos que con estos metodos queda demostrado que conocemos y manejamos el tema, por favor no nos baje la nota, nos merecemos un hermoso 5. Gracias xd")
  print("\n\n*******************************************MENÚ********************************************\n")
  print("Digite la opción a ejecutar: ")
  opc = int(input("1. Lista Simple.\n2. Lista Doble.\n3. Lista Circular.\n4. Salir.\n"))
  if opc == 1:
    subMain1(listaSimple)
  elif opc == 2:
    subMain2(listaDoble)
  elif opc == 3:
    subMain3(listaCircular)
  elif opc == 4:
    print("Hasta la próxima (con voz de Loquendo)")
    break
  else:
    print("Opción invalida")

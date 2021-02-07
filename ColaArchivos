class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node(int(input("Introducir cedula\n")))
e2 = Node(input("Introduce el codigo del examen \n"))
e3 = Node(input("Introduce el la descripción \n"))

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Agrega al final")

list.listprint()

def subMain2():
  cola = ColaReales()
  while True:
    print("\n\n*******************************************REGISTRO DE EXAMENES*******************************************\n")
    print("Digite la opción a ejecutar: ")
    opc = int(input("1. Ingrese un nuevo examen negado.\n2.Buscar registro .\n3. Mostrar registros realizados.\n"))
    if opc == 1:
      if cola.isFull():
        print("La lista esta llena")
      else:
        n = float(input("Ingrese un nuevo registro\n"))
        cola.queue(n)
        print(n, " el registro fue realizado exitosamente")
      elif opc == 2:
      if cola.isEmpty():
        print("No hay elementos registrados")
      else:
        print("Busque un registro ", cola.getFirst())
    elif opc == 3:
      print("A continuación la información de acuerdo a la busqueda realizada ", cola.getNumberOfElements(), " elementos")
        break

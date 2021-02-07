import numpy as np

def llenarMatriz(tamano):
  i = 0
  matriz = np.empty([tamano,2], dtype = str)
  while i < tamano:
    matriz[i, 0] = input("individuo: \n")
    matriz[i, 1] = input("funcion de adaptación para el individuo: \n")
    i = i + 1
  return np.array(matriz)
  
  def torneoDeterminista(matriz):

  aleatorio = []
  i = 1
  while i < 4:
    x = np.random.randint(0, len(matriz))
    if x not in aleatorio:
      aleatorio.append(x)
      i+=1
  
  gladiador = [matriz[aleatorio[0]][0], matriz[aleatorio[1]][0], matriz[aleatorio[2]][0]]
  adaptacion = [int(matriz[aleatorio[0]][1]), int(matriz[aleatorio[1]][1]), int(matriz[aleatorio[2]][1])]

  if adaptacion[0] == adaptacion[1] == adaptacion[2]:
    torneoDeterminista(matriz)
  else:
    print("************************************************************************")
    print("Individuos a enfrentar: ", gladiador[0], ", ", gladiador[1], ", ", gladiador[2])
    print("Funciones evaluadas: ", adaptacion[0], ", ", adaptacion[1], ", ", adaptacion[2])
    maxi = max(adaptacion)
    print("Máxima adaptabilidad: ", maxi)
    index = adaptacion.index(maxi)
    ganador = gladiador[index]
    print("\nEL INDIVIDUO SELECCIONADO ES: ", ganador)
    print("************************************************************************\n")
    
    def torneoProbabilistico(matriz, nAleatorio):

  aleatorio = []
  i = 1
  while i < 4:
    x = np.random.randint(0, len(matriz))
    if x not in aleatorio:
      aleatorio.append(x)
      i+=1
  
  gladiador = [matriz[aleatorio[0]][0], matriz[aleatorio[1]][0], matriz[aleatorio[2]][0]]
  adaptacion = [int(matriz[aleatorio[0]][1]), int(matriz[aleatorio[1]][1]), int(matriz[aleatorio[2]][1])]
  sumatoriaAdaptacion = adaptacion[0] + adaptacion[1] + adaptacion[2]
  probabilidad = [adaptacion[0]/sumatoriaAdaptacion, adaptacion[1]/sumatoriaAdaptacion, adaptacion[2]/sumatoriaAdaptacion]
  print("*************************************************************************")
  print("Individuos a enfrentar: ", gladiador[0], ", ", gladiador[1], ", ", gladiador[2])
  print("Funciones evaluadas: ", adaptacion[0], ", ", adaptacion[1], ", ", adaptacion[2])
  print("Suma adaptaciones: ",sumatoriaAdaptacion)
  print("Probabilidades asociadas: ", probabilidad)
  
  q1 = np.zeros(3)
  for b in range(len(probabilidad)):
    q1[b] += q1[b-1] + probabilidad[b] 
  print("Matriz q1: ",q1)
  q1 = np.insert(q1, 0, 0)

  print("Areglo de números aleatorios: ", nAleatorio)
  n = 0
  x = 0
  for n in range(1, len(probabilidad) + 1):
    if q1[n - 1] <= nAleatorio <= q1[n]:
      print("\nEL INDIVIDUO SELECCIONADO ES: ", gladiador[n - 1])
      print("************************************************************************\n")
      break  
      
      
      def muestreoResto(matriz, k):
  n = 0
  e = 0
  for e in range(len(matriz)):
    n += int(matriz[e][1])
  print("************************************************************************")
  print("Sumatoria de las funciones de adaptación:  ",n)
  p1 = np.zeros(tamano)
  a = 0
  for a in range(len(matriz)):
    p1[a] = round(int(matriz[a][1])/n, 2)

  print("Matriz p1:  ",p1)
  pik = p1*k
  print("Matriz p1*k: ",pik)
  for i in range(len(pik)):
    if pik[i] >= 1:
      print("\nEL INDIVIDUO SELECCIONADO ES: ", matriz[i][0])
      print("************************************************************************\n")
      k -= 1
  if k != 0:
    for i in range(k):
      torneoDeterminista(matriz)
      def seleccionRuleta(tamano, matriz, hijos):
  n = 0
  e = 0
  for e in range(len(matriz)):
    n += int(matriz[e][1])
    #e = e + 1 
  print("Sumatoria de las funciones de adaptación: ",n)
  p1 = np.zeros(tamano)
  q1 = np.zeros(tamano)
  a = 0
  for a in range(len(matriz)):
    p1[a] = round(int(matriz[a][1])/n, 2)
  mt = np.transpose(matriz)
  print("Individuos           : ", mt[0])
  print("Funcion de Adaptacion: ", mt[1])
  print("Matriz p1            : ",p1)
  for b in range(len(p1)):
    q1[b] += q1[b-1] + p1[b]
  print("Matriz q1            : ",q1)
  q1 = np.insert(q1, 0, 0)
  nAleatorio = np.random.rand(hijos)
  print("Areglo de numeros aleatorios: ",nAleatorio)
  n = 0
  x = 0
  for i in nAleatorio:
    for n in range(1, len(p1) + 1):
      if q1[n - 1] <= i <= q1[n]:
        print("\nEl individuo seleccionado es: \n", matriz[n - 1][0])
        break
    
    while True:
  print("\n\n*******************************************MENÚ********************************************\n")
  print("Digite la opción a ejecutar: ")
  opc = int(input("1. Ingresar Parámetros.\n2. Metodo de selección.\n3. Salir \n"))
  if opc == 1:
    tamano = int(input("\nIngrese el tamaño de la población\n"))
    print("Ingrese los individuos y su función de adaptación:\n")
    m = llenarMatriz(tamano)  
  elif opc == 2:
    print("\n\n******************Metodo de selección***********************\n")
    opc2 = int(input("1. Selección Ruleta.\n2. Muestreo probabilistico.\n3. Selección por Torneo Determinista. \n4. Muestreo por restos:\n"))
    if opc2 == 1:
      print("Selección Ruleta")

      hijos = int(input("Ingrese la cantidad de hijos deseados: \n"))
      seleccionRuleta(tamano, m, hijos)
    elif opc2 == 2:
      print("Selección probabilistico")
      hijos = int(input("Ingrese la cantidad de hijos deseados: \n"))
      for i in range(hijos):
        print("TORNEO: ", i+1)
        torneoProbabilistico(m, np.random.rand(1))
    elif opc2 == 3:
      print("Selección por Torneo Determinista")
      hijos = int(input("Ingrese la cantidad de hijos deseados: \n"))
      for i in range(hijos):
        print("TORNEO: ", i+1)
        torneoDeterminista(m)
    elif opc2 == 4:
      print("Muestreo por restos")
      k = int(input("Ingrese la cantidad de hijos deseados:\n"))
      muestreoResto(m, k)
  elif opc == 3:
    print("Hasta luego.")
    break
  else:
    print("Opción invalida")

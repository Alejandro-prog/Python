import math as mt
 
""" 
Esta función genera todos los números Gray 
codifica e imprime los códigos generados
"""
def generarArregloGray(numero):
 
    # Caso base
    if (numero <= 0):
        return print('El número no puede ser menor o igual a 0')
 
    # (arreglo) almacenará todos los códigos generados
    arreglo = list()
 
    # empezar con un patrón de un bit
    arreglo.append("0")
    arreglo.append("1")
 
    """
    Cada iteración de este bucle genera
    2 * y códigos, y codigos generados previamente.
    """
    y = 2
    q = 0
    while(True):
 
        if y >= 1 << numero:
            break
     
        """
        Ingresa los códigos generados anteriormente 
        en el nuevo arreglo[] en orden inverso. 
        """
        for q in range(y - 1, -1, -1):
            arreglo.append(arreglo[q])
 
        # agregar 0 a la primera mitad
        for q in range(y):
            arreglo[q] = "0" + arreglo[q]
 
        # agregar 1 a la segunda mitad
        for q in range(y, 2 * y):
            arreglo[q] = "1" + arreglo[q]
        y = y << 1
 
    # contenido de arreglo []
    for y in range(len(arreglo)):
        print(arreglo[y])
 
# llamanos al metodo
generarArregloGray(5)

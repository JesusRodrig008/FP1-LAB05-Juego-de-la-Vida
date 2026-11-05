import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    # TODO: Ejercicio 1
    lista = []
    for i in range (filas):
        lista_aux=[]
        for i in  range(columnas):
                 
            lista_aux.append(False)
        lista.append(lista_aux)
    return lista

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    # TODO: Ejercicio 2
    lista = []
    for i in range (filas):
        lista_aux=[]
        for i in  range(columnas):
            if random.random() < probabilidad_vida: 
                lista_aux.append(True)
            else:
                lista_aux.append(False)
        lista.append(lista_aux)
    return lista
    

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """
    # TODO: Ejercicio 3
    
    for i_fila in range (len(patron)):

        for i_columna in range(len(patron[i_fila])):
            
            pos_fila_real = pos_fila + i_fila
            pos_col_real = pos_col + i_columna
            if pos_fila_real <= len(tablero) and pos_col_real <= len(tablero[i_fila]):
                tablero[pos_fila_real][pos_col_real] = patron[i_fila][i_columna]
    
    pass

def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    # TODO: Ejercicio 4
    vecinos_vivos = 0
    for i in range (-1,2):
        for j in range(-1,2):
            if not( i == 0 and j == 0):
                
                if tablero[(i+fila)%len(tablero)][(j+col)%len(tablero[fila])] == True:
                    vecinos_vivos += 1
    return vecinos_vivos

def calcular_siguiente_generacion(tablero) -> list[list[bool]]:
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    # TODO: Ejercicio 5
    res = crear_tablero(len(tablero), len(tablero[0]))
    for i_fila in range(len(tablero)):
        for i_col in range(len(tablero[i_fila])):
            vecinos = contar_vecinos(tablero,i_fila,i_col)
            if vecinos == 3:
                res[i_fila][i_col] = True
            elif vecinos == 2:
                res[i_fila][i_col] = tablero[i_fila][i_col]
            else:
                res[i_fila][i_col] = False
    return res

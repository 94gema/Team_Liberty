import numpy as np
import random

#1. CLASE TABLERO [Genma]
class Tablero():      #[Genma] Usado para Tablero1 y Tablero2
    def __init__(self, tamaño = 10):
        self.tamaño = tamaño
        
    def tablero_player1(self, tamaño):
        t1 = np.full((tamaño,tamaño), " ")
        return t1  #[Genma]Variable local
    
    def tablero_player2(self, tamaño):
        t2 = np.full((tamaño,tamaño), " ")
        return t2  #[Genma]Variable local
    
# (SORAYA): He empezado a crear la clase, he puesto por defecto los barcos ya con sus posiciones. Lo he tenido que hacer de esta forma (lista de listas)
# porque de uno en uno era más trabajoso a la hora de hacer la funcion 'coloca_barco'


#Falta hacer colocar la máquina de forma aleatoria los barcos. Supongo que aquí hará falta el costructor __init__

#5. CLASE BARCOS [Genma] Uso los mismos barcos para los dos tableros de momento
class Barco:  #[Gustavo]
    
    barcos = [[(0,1), (4, 3), (8, 8), (7, 1)], # barco1 (1 esolora x 4)
              [(2,2), (2,1), (5,6), (4,6), (9,6), (9,5)], # barco2 (2 esloras x 3)
              [( 9,1), (9,2), (9,3), (0,7), (1,7), (2,7)], # barco3 (3 esloras x 2)
              [(7,3), (7,4), (7,5), (7,6)]] # barco4 (4 esloras x 1)
    
    def __init__(self): #, nombre, longitud):   Dejo el init para intentar el barco aleatorio
        pass#self.nombre = nombre
        #self.longitud = longitud

    def coloca_barco(self, tablero):   #[Genma] Usado para tablero 1 y 2 de momento
        for barco in self.barcos:
            for pieza in barco:
                tablero[pieza] = "O"
        return tablero
    
    def crea_barco_aleatorio(self, tablero):  #[Genma] Pendiente de que funcione
        global barcos_player2
        for barco in barcos_player2:
            longitud = barco.longitud
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            orientacion = random.choice(["N", "S", "E", "O"])
            if orientacion == "N": 
                if fila - longitud >= 0: 
                    if all(tablero[fila:fila + longitud, columna] == " "):
                        tablero[fila:fila + longitud, columna] = "O" 
            if orientacion == "S":
                if fila + longitud <= len(tablero):
                    if all(tablero[fila:fila + longitud, columna] == " "):                  
                        tablero[fila:fila + longitud, columna] = "O"
            if orientacion == "E":
                if columna + longitud <= len(tablero):
                    if all(tablero[fila, columna:columna + longitud] == " "):
                        tablero[fila, columna:columna + longitud] = "O"
            if orientacion == "O":
                if columna  - longitud >= 0:
                    if all(tablero[fila, columna:columna + longitud] == " "):
                        tablero[fila, columna:columna + longitud] = "O"
            return tablero



    
    
'''

# Gustavo

Chicos no soy capaz de colocar los barcos aleatoriamente.
Sí he podido hacer las funciones de disparar y de comprobar si hay barcos en el tablero.
lo he dejado en funciones

  
'''



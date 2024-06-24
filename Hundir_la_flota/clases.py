import numpy as np
from Hundir_la_flota import variables 

class Tablero():
    def __init__(self, tamaño = 10):
        self.tamaño = tamaño
        
    def tablero_player1(self, tamaño):
        tablero1 = np.full((tamaño,tamaño), " ")
        return tablero1
    
    def tablero_player2(self, tamaño):
        tablero2 = np.full((tamaño,tamaño), " ")
        return tablero2
    
# (SORAYA): He empezado a crear la clase, he puesto por defecto los barcos ya con sus posiciones. Lo he tenido que hacer de esta forma (lista de listas)
# porque de uno en uno era más trabajoso a la hora de hacer la funcion 'coloca_barco'

'''
Falta hacer colocar la máquina de forma aleatoria los barcos. Supongo que aquí hará falta el costructor __init__
'''

class Barco:
    
    barcos = [[(0,1), (4, 3), (8, 8), (7, 1)], # barco1 (1 esolora x 4)
              [(2,2), (2,1), (5,6), (4,6), (9,6), (9,5)], # barco2 (2 esloras x 3)
              [( 9,1), (9,2), (9,3), (0,7), (1,7), (2,7)], # barco3 (3 esloras x 2)
              [(7,3), (7,4), (7,5), (7,6)]] # barco4 (4 esloras x 1)

    def coloca_barco(self, tablero):
        for barco in self.barcos:
            for pieza in barco:
                tablero[pieza] = "O"
        return tablero
    


# Gustavo
    '''
Chicos no soy capaz de colocar los barcos aleatoriamente.
Sí he podido hacer las funciones de disparar y de comprobar si hay barcos en el tablero.
lo he dejado en funciones
    '''
  




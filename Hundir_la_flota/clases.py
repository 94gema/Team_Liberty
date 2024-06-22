import numpy as np


class Tablero():
    def __init__(self, tamaño = 10):
        self.tamaño = tamaño
        
    def tablero_player1(self, tamaño):
        tablero1 = np.full((tamaño,tamaño), " ")
        return tablero1
    
    def tablero_player2(self, tamaño):
        tablero2 = np.full((tamaño,tamaño), " ")
        return tablero2
    

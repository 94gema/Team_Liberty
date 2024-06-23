from Hundir_la_flota import clases 

player1 = input("Introduzca su nombre")
player2 = "computadora"

vidas1 = 20
vidas2 = 20


# (SORAYA) He creado los tableros dentro de la clase.
tablero1 = Tablero(10) 
tablero1 = tablero1.tablero_player1(10)

barcos = Barco()

tablero1 = barcos.coloca_barco(tablero1)

tablero1

tablero2 = Tablero(10)
tablero2.tablero_player2(10)






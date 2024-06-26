from clases import*

#2. VARIABLES TABLERO VACIO [Genma]
# (SORAYA) He creado los tableros dentro de la clase.
tablero1 = Tablero() 
tablero1 = tablero1.tablero_player1(10)

tablero2 = Tablero(10)
tablero2 = tablero2.tablero_player2(10)


#3.VARIABLES PARA FUNCION BIENVENIDA [Genma] 
player1 = input("Introduzca su nombre:")  #[Genma] Usado en funcion bienvenida
player2 = "computadora" #[Genma] Usado en funcion bienvenida


#6. VARIABLES BARCO [Genma]
barcos_player1 = Barco()   #Victor
barcos_player2 = Barco()   #[Genma] Duplico hasta que pongamos barcos aleatorios

'''[Genma]Lo dejo para pruebas para barco aleatorio  
barcos_player2 = [    #Victor
    Barco("barco1", 1),
    Barco("barco2", 1),
    Barco("barco3", 1),
    Barco("barco4", 1),
    Barco("barco5", 2),
    Barco("barco6", 2),
    Barco("barco7", 2),
    Barco("barco8", 3),
    Barco("barco9", 3),
    Barco("barco10", 4)
]
'''


#7. VARIABLE PARA POSICIONAR BARCOS [Genma]  Estan vacios pero se posicionaran los barcos despues en una funcion
tablero1_barco = tablero1.copy()     
tablero2_barco = tablero2.copy() 


#10 VARIABLES VIDAS #Víctor, antes tenían 2 vidas. Realmente son 20 una por cada posición que tienen los barcos
vidas1 = 20
vidas2 = 20





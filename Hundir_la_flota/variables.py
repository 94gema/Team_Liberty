import clases
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


#7. VARIABLE PARA POSICIONAR BARCOS [Genma]
tablero1_barco = tablero1.copy()  
tablero2_barco = tablero2.copy() 


#10 VARIABLES VIDAS
vidas1 = 2
vidas2 = 2


'''
Hola equipo, soy Victor

Añadí a variables "from clases import*" porque salía un mensaje al lado de tablero1 y tablero2 que no estaban definidos.

Al final del documento del hundir la flota comenta en el punto 8 de Recomendaciones que si no tenemos un nivel
alto coloquemos los barcos en posicones fijas. 
Yo iría por ese camino, como dice Soraya para no complicarnos la vida más de lo que la tenemos.
En la sección de funciones he añadido una función personalizada def para comenzar el juego. Esta en pañales.
La he creado porque la función de contador de vida debería estar dentro de una función que gestione el juego.
Es una guia, modificarla y tunearla todo lo que necesiteis, me he estado rompiendo los cuernos en como hacer 
la función contador de vidas, realmente no es una función sola sino que tendremos que fusionar tanto la de disparo, tablero y la de vida.
Vamos en otras palabras que no son funciones independientes, desde mi punto de vista.
Según vaya haciendola después las fusionamos.
'''




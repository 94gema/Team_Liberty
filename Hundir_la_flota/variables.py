from Hundir_la_flota import clases 
from clases import*

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

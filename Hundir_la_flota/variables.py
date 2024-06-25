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


#10 VARIABLES VIDAS #Víctor, antes tenían 2 vidas. Realmente son 20 una por cada posición que tienen los barcos
vidas1 = 20
vidas2 = 20
'''
Víctor
Editado 25/06
Informe de misión xD
Se me ha ido todo el tiempo en probar el juego y modificar algunas parte del código. 
Sino me equivoco todas las líneas modificadas estan comentadas y aquellas funciones que estaban antes las he dejado entre comillas.
Por si alguien ve una manera más efectiva y menos engorrosa

He modificado el campo cuando se falla y he puesto una A en lugar _, al practicar me estaba dejando la vista y no daba pie con bola


Queda pendiente aún poner los barcos de forma aleatoria.
Sería bueno que creemos una opción para terminar la partida sin tener que llegar a quitar las vidas a la maquina
Jugando confirmo que la maquina quita vidas pero no estoy seguro de si repite turno.

Cuando se introduce una combinación fuera del 0 al 9 te dice que introduzcas una buena pero después sale un mensaje de error en el script funciones
en la línea 46 con el siguiente mensaje:


Se produjo una excepción: UnboundLocalError
local variable 'columna' referenced before assignment
  File "C:\Users\Victor\Desktop\Bootcamp\DS_Online_Mayo24\Team_Liberty\Hundir_la_flota\funciones.py", line 46, in coordenadas_disparo
    if (fila < 1) or (fila > 10) or (columna < 1) or (columna > 10):
  File "C:\Users\Victor\Desktop\Bootcamp\DS_Online_Mayo24\Team_Liberty\Hundir_la_flota\funciones.py", line 102, in disparar
    fila_disparo, columna_disparo = coordenadas_disparo()
  File "C:\Users\Victor\Desktop\Bootcamp\DS_Online_Mayo24\Team_Liberty\Hundir_la_flota\funciones.py", line 172, in jugar
    acierto = disparar(tablero2, tablero2_barco)
  File "C:\Users\Victor\Desktop\Bootcamp\DS_Online_Mayo24\Team_Liberty\Hundir_la_flota\main.py", line 10, in <module>
    jugar()
UnboundLocalError: local variable 'columna' referenced before assignment
'''







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




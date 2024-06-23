from Hundir_la_flota import clases 

player1 = input("Introduzca su nombre")
player2 = "computadora"

vidas1 = 20
vidas2 = 20


# (SORAYA) He creado los tableros dentro de la clase.
tablero1 = Tablero(10) # type: ignore
tablero1.tablero_player1(10)


tablero2 = Tablero(10) # type: ignore
tablero2.tablero_player2(10)

'''
(SORAYA)

Los tipos de barcos se deberían de crear dentro de la clase Barco, es lo que me cuadra más, porque entonces tendría que hacer un bucle para crear la longitud
y creando una función dentro de la clase bastaría y sería más fácil para luego hacer otra función para posicionarlos en el tablero en plan:
    Dentro de la clase de barcos crear unos constructores que sea self.nombre, self.longitud, self.posiciones (para donde se quiere posicionar).. no?
    y cuando tengamos ya la clase, los barcos ya se ponen aquí, importando aquí:

    >>> barco1 = Barco("barco1", 4, posiciones = [(0,1), (0,2), (0,3), (0,4)]) --> Ejemplo

    o dar unas posiciones fijas para el humano y ya marcarlas aquí, como lo veis? y nos complicaríamos muchuísimo menos    
'''




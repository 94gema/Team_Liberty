from clases import*
from variables import*
import random
import variables


#1. CLASE TABLERO [Genma]
#2. VARIABLES TABLERO VACIO [Genma]
#3. VARIABLES PARA FUNCION BIENVENIDA [Genma] 


#4. FUNCION 1[Genma]
def bienvenida():  #[Genma] Presentación del juego. Paso 1 en main
    global player1, player2
    print("\n¡Bienvenido a hundir la flota ", player1, "!", sep="")
    print("\nSu oponente será la ", player2, ". Que gane el mejor.\n", sep="")
    print("Los tableros de ambos jugadores serán una cuadrícula de 10x10.")
    input(f"{player1}, tú y la máquina tendreis cada uno un tablero como este:\n\n {tablero1}\n\n\tPulsa intro para posicionar tus barcos.")
   

#5. CLASE BARCOS [Genma] Uso los mismos barcos para los dos tableros de momento
#6. VARIABLES BARCO [Genma]
#7. VARIABLE PARA POSICIONAR BARCOS [Genma]


#8. POSICIONAR BARCOS EN TABLERO [Genma]
def colocar_barcos():
    global tablero1_barco, tablero2_barco, barcos_player1, barcos_player2
    tablero1_barco = barcos_player1.coloca_barco(tablero1_barco)  #Soraya
    print("\n",player1, "la posición de tus barcos es la siguiente:")
    print(tablero1_barco)

    tablero2_barco = barcos_player2.coloca_barco(tablero2_barco)  #Soraya  [Genma] Duplico hasta que pongamos barcos aleatorios
    #tablero2_barco = barcos_player2.crea_barco_aleatorio(tablero2) #Soraya [Genma]Lo dejo para pruebas de barco aleatorio
    #print(tablero2_barco)  #para comprobación
    input("\n\tPresiona Intro para empezar a disparar.")


#9. CONTROL DE ERRORES Y PETICIÓN DE FILA COLUMNA 
def coordenadas_disparo():  #[Genma] Añado los inputs y el control de errores
    try:       
        fila= int(input("Numero de fila donde quieres disparar del 1 al 10: "))
        columna = int(input("Numero de columna donde quieres disparar del 1 al 10: "))
    except:
        print("\n\tPor favor, introduce un número del 1 al 10, vuelve a intentarlo.\n")
        coordenadas_disparo()
    if (fila < 1) or (fila > 10) or (columna < 1) or (columna > 10):
        print("\n\tPor favor, introduce un numero del 1 al 10, vuelve a intentarlo.\n")
        coordenadas_disparo()
    else:
        print(f"\tEl disparo se efectuará en la coordenada: ({fila},{columna})")
        return fila, columna     #[Genma]Variables locales


#10. VARIABLES VIDAS

#11. CONTADOR DE VIDAS [Genma]
def contador_vidas(vidas):
    global vidas1, vidas2
    if vidas1 == 0:
        print("Ohhh has perdido, gana la", player2)
        return False
    elif vidas2 == 0:
        print("Enhorabuena!!! Has ganado a la", player2)
        return False
    else:
        print(f"{player1} tiene {vidas1} vidas y {player2} tiene {vidas2} vidas.")
        return True

#12. DISPARAR JUGADOR
def disparar(tablero, tablerobarco): #[Genma]Siempre disparará al tablero2_agua
    global tablero2, tablero2_barco, vidas2
    fila_disparo, columna_disparo = coordenadas_disparo()
# Comprueba si el disparo es un impacto
    #SI HAY IMPACTO
    if tablero2_barco[fila_disparo-1][columna_disparo-1] == 'O':   #[Genma] Añado -1 para pensar como humanos y no como maquinas. Buscamos en tablero barco y marcamos en el vacio
        tablero2[fila_disparo-1][columna_disparo-1] = 'X'  # Marca el impacto
        print(f"\nEl jugador {player1} ha acertado. Ha quitado una vida a {player2}.")
        vidas2 = vidas2 - 1
        vidas = contador_vidas(vidas2)
        acierto = True
        print("\nAsi queda el tablero del", player2,"\n",tablero2)
        if acierto == True:
            return True
        else:
            return False
    #CUANDO NO HAY IMPACTO
    else:
        tablero2[fila_disparo-1][columna_disparo-1] = '-'  # Marca el fallo
        print(f"\nEl jugador {player1} no ha acertado.")
        print("\nAsi queda el tablero del", player2,"\n",tablero2)
        return False


#13. DISPARAR MAQUINA  [Genma] No lo he pronado.
def disparar_maquina(tablero,tablerobarco): #[Genma]Siempre disparará al tablero1_agua
    global tablero1, tablero1_barco, vidas1
    fila = random.randint(0,9)
    columna = random.randint(0,9)
# Comprueba si el disparo es un impacto
    #CUANDO SI HAY IMPACTO
    if tablero1_barco[fila][columna] == 'O':   #[Genma] Quito el  -1 porque ya pensamos como la maquina
        tablero1[fila][columna] = 'X'  # Marca el impacto
        print(f"El jugador {player2} ha acertado. Ha quitado una vida a {player1}")
        vidas1 = vidas1 -1
        vidas = contador_vidas(vidas1)
        acierto = True
        print("\nAsi queda el tablero del", player1,"\n",tablero1)
        return vidas, acierto
    #CUANDO NO HAY IMPACTO
    else:
        tablero1[fila][columna] = '-'  # Marca el fallo
        print(f"\nEl jugador {player2} no ha acertado.")
        print("\nAsi queda el tablero del", player1,"\n",tablero1)
        vidas == True
        acierto == False
        return vidas, acierto

#14 FUNDICON BUCLE
def jugar():
    global vidas
    while True:
        vidas, acierto = disparar(tablero2, tablero2_barco)
        if vidas == False:
            break
        elif acierto == False:
            break
        else:
            continue
    #while True:
        #disparar_maquina(tablero1, tablero1_barco)
    jugar()


#QUEDAN BARCOS?      [Genma] Creo que está no hace falta con el contador de vidas.
def hay_barcos(tablero):
    # Comprueba si quedan barcos en el tablero
    for fila in tablero:
        if 'B' in fila:
            return True
    return False




'''
def jugar_juego(jugador_turno, vidas_otro_jugador,tablero):
#Tenemos que crear una función para jugar que incluya todas las funciones. 
#Esta que he creado es orientativa la necesitaba para guiarme en la función por turnos

#función vida
while vidas1 > 0 and vidas2 > 0:   #el mensaje de bloque con sangría es porque arriba está la función def jugar_juego
    print("Turno del jugador 1. Vidas :{vidas1}")
    print("Turno del jugador 2. Vidas; {vidas2}")  
    #Aquí definiria la función de los turnos
    while True:
        if vidas1 <= 0:
            print(f"{player2} ha gando. El judador 1 se ha quedado con {vidas1} vidas")
            break
        elif vidas2 <= 0:
            print(f"{player1} he ganado. El judador 2 se ha quedado con {vidas2} vidas")
            break
        else:
            if vidas1 > vidas2: #REVISAR NOTAS# Empieza el turno el jugador 1, se define argumentos de la función del juego
                jugador_turno = player1
                otro_jugador = player2
                vidas_otro_jugador = vidas2
                tablero = tablero2
            else:
                jugador_turno = player2
                otro_jugador = player1
                vidas_otro_jugador = vidas1
                tablero = tablero1
            while True:
                acierto = jugar_juego(jugador_turno, vidas_otro_jugador, tablero)
                if acierto == True: 
                    vidas_otro_jugador -= 1
                    print(f"El jugador {jugador_turno} ha acertado. Ha quitado una vida a {otro_jugador}")
                    continue              
                else:
                    print(f"El jugador {jugador_turno} ha fallado. Cambio de turno al {otro_jugador}")
                    break

                    
                    No tengo muy clara esta última parte si termina de funcionar. Lo he intentado probar en python tutor pero antes me pide tableros y otras 
                    funciones que aún no estan definidas. 

                    Esto de aquí acabo es una alternativa al final de la función turnos que aún tengo que pulir si no funciona lo de arriba 
                    else:
                        print("Es turno de "({player2 if jugador_turno == player1 if not player1})
                        break
                                                               
    print("El juego ha terminado")


    # Funciones para disparar y comprobar si hay barcos
'''







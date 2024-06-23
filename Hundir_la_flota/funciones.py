from variables import*
from clases import*



def jugar_juego(jugador_turno, vidas_otro_jugador,tablero):
#Tenemos que crear una función para jugar que incluya todas las funciones. Esta que he creado es orientativa la necesitaba para guiarme en la función por turnos

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

                    '''
                    No tengo muy clara esta última parte si termina de funcionar. Lo he intentado probar en python tutor pero antes me pide tableros y otras 
                    funciones que aún no estan definidas. 

                    Esto de aquí acabo es una alternativa al final de la función turnos que aún tengo que pulir si no funciona lo de arriba 
                    else:
                        print("Es turno de "({player2 if jugador_turno == player1 if not player1})
                        break
                      '''                                            
    print("El juego ha terminado")


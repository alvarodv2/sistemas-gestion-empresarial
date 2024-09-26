'''
Clase quixo. El quixo es un juego de mesa similar al 3 en raya. Crea una clase para poder jugar partidas 
contra una IA. En realidad para la IA simplemente busca una jugada aleatoria que sea legal. La primera 
mejora de la IA sería que esa jugada legal no hace que pierda la IA. La segunda mejora sería que si 
existe una jugada con la que la IA puede ganar, que haga esa jugada.
Aquí tienes un vídeo de como se juega.
https://youtu.be/F2kuj1qlaKk?si=fftHkcQaM5j3L7jd
'''

import random

class Quixo:
    def __init__(self):
        self.tablero = [[' ' for _ in range(5)] for _ in range(5)]

    def mostrarTabla(self):
        print("    0   1   2   3   4")
        print("  --------------------- ")
        for i, fila in enumerate(self.tablero):
            print(f"{i} | {' | '.join(fila)} | ")
            print("  --------------------- ")

    def mover(self, fila, columna, jugador):
        # Verificamos que el movimiento sea valido (borde del tablero)
        if fila in [0, 4] or columna in [0, 4]: 
            if self.tablero[fila][columna] == ' ':
                self.tablero[fila][columna] = jugador
            else:
                print("Casilla ocupada")
        else:
            print("Movimiento no valido")

    def jugada_aleatoria(self):
        # Generar una lista de movimientos posibles (bordes del tablero)
        movimientos_posibles = [(fila, columna) for fila in [0, 4] for columna in range(5)] + \
                               [(fila, columna) for fila in range(5) for columna in [0, 4]]
        # Filtrar movimientos que sean válidos (casillas vacías)
        movimientos_validos = [(fila, columna) for fila, columna in movimientos_posibles if self.tablero[fila][columna] == ' ']
        # Elegir un movimiento aleatorio de los válidos
        return random.choice(movimientos_validos) if movimientos_validos else None

    def jugarJuego(self):
        turno = 'X'
        while True:
            self.mostrarTabla()
            if turno == 'X':
                fila = int(input(f"Jugador {turno}, ingrese la fila (0-4): "))
                columna = int(input(f"Jugador {turno}, ingrese la columna (0-4): "))  
            else:
                # Generar jugada aleatoria para la IA
                movimiento = self.jugada_aleatoria()
                if movimiento:
                    fila, columna = movimiento
                    print(f"IA juega en fila {fila}, columna {columna}")
                else:
                    print("No hay movimientos válidos para la IA")
                    break

            self.mover(fila, columna, turno)

            # Cambiar de turno
            turno = 'O' if turno == 'X' else 'X'

juego = Quixo()
juego.jugarJuego()


def verificar_ganador(self, jugador):
    # Verificar filas y columnas
    for i in range(5):
        if all(self.tablero[i][j] == jugador for j in range(5)) or all(self.tablero[j][i] == jugador for j in range(5)):
            return True
    # Verificar diagonales
    if all(self.tablero[i][i] == jugador for i in range(5)) or all(self.tablero[i][4-i] == jugador for i in range(5)):
        return True
    return False

def jugarJuego(self):
    turno = 'X'
    while True:
        self.mostrarTabla()
        if turno == 'X':
            fila = int(input(f"Jugador {turno}, ingrese la fila (0-4): "))
            columna = int(input(f"Jugador {turno}, ingrese la columna (0-4): "))  
        else:
            movimiento = self.jugada_aleatoria()
            if movimiento:
                fila, columna = movimiento
                print(f"IA juega en fila {fila}, columna {columna}")
            else:
                print("No hay movimientos válidos para la IA")
                break

        self.mover(fila, columna, turno)

        if self.verificar_ganador(turno):
            self.mostrarTabla()
            print(f"Jugador {turno} ha ganado la partida")
            break

        turno = 'O' if turno == 'X' else 'X'
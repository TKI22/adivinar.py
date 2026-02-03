
nombre1 = input("Jugador 1 ¿Cuál es tu nombre?: ")
nombre2 = input("Jugador 2 ¿Cuál es tu nombre?: ")
print()

jugador1 = input(f"Hola {nombre1}, ¿Qué eliges? ¿Piedra, Papel o Tijera?: ").lower
jugador2 = input(f"Hola {nombre2}, ¿Qué eliges? ¿Piedra, Papel o Tijera?: ").lower
print()

if jugador1 == jugador2:
    print("¡Empate!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print(f'"{nombre1}" Ganó!')
else:
    print(f'"{nombre2}" Ganó!')

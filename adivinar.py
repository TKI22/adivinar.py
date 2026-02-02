import random


numero_secreto = random.randint(1,101)
adivinado = False
intentos = 0
intentos_maximos = 5

print("Bienvenido! Adivina un numero entre 1 a 100")

while not adivinado:
    if intentos >= intentos_maximos:
        print("Fallaste, cantidad maxima de intentos alcanzada")
        break

    numero = int(input("Adivina el numero: "))

    if numero == numero_secreto:
        print(f"Adivninaste! el numero era {numero_secreto}")
        adivinado = True

    elif numero < numero_secreto:
        print(f"El numero secreto es mas grande que {numero}")

    else:
        print(f"El numero secreto es mas pequeño que {numero}")
    
    intentos += 1


import random
numero = random.randint(1, 50) 
vidas = 10 
nombre = input("Bienvenido al juego de adivinar el número, ¿Cuál es tu nombre? ")
print("Todo listo? " + str(nombre) + ". Empecemos, tienes 10 intentos para adivinar el número que estoy pensando. ")
print("Adivina el número entre 1 y 50")
while vidas > 0:
    adivinanza = int(input("Digita el número : "))    
    if adivinanza == numero:
        print("¡Has adivinado el número! ¡Has ganado el juego!")
        break
    else:
        vidas = vidas - 1
        if adivinanza < numero:
            print("El número que debes adivinar es mayor, siguelo intentando")
        else:
            print("El número que debes adivinar es menor, siguelo intentando")
        print(" Has fallado, te quedan " + str(vidas) + " vidas")
if vidas == 0:
    print("Has perdido, te has quedado sin Intentos. El número era " + str(numero))
print("Fin del juego")



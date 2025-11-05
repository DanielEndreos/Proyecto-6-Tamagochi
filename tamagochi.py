### Objetivo: Crear un programa que simule una mascota virtual, aplicando funciones, 
# bucles, condicionales, variables globales y eventos aleatorios.

#Requisitos:
#Variables de estado
#energia, felicidad, hambre, acciones.
#Inicializa con valores aleatorios entre 3 y 5 para que sea mas dinámico.

import random
import time

class Tamagochi():

    def __init__(self):
        self.nombre     = "Not defined"
        self.energia    = random.randint(3,5)     #Variable de Estado - Energía: random 3-5
        self.felicidad  = random.randint(3,5)     #Variable de Estado - Felicidad: random 3-5
        self.hambre     = random.randint(3,5)     #Variable de Estado - Hambre: random 3-5
        self.acciones   = 0                       #Variable de Estado - Acciones: 0 

    #Funciones
    #nombrarTamagochi() -> Solicita al usuario mediante input() el nombre del bicho.
    def nombrarTamagochi(self):
        inputName = input("Introduce un nombre para tu Tamagochi:")
        self.nombre=inputName

    #mostrar_estado() → imprime todos los estados actuales. imprime: ❤️ Felicidad: ⚡ Energía: 🍖 Hambre:                                   
    def mostrar_estado(self):
        print(f"\n❤️ Felicidad: {self.felicidad} ⚡ Energía: {self.energia} 🍖 Hambre: {self.hambre}")

    #comer() → reduce hambre en 3, aumenta felicidad en 1, reduce energía en 1. imprime: está comiendo 🍗
    def comer(self):
        print(f"\n{self.nombre} está comiendo 🍗")
        self.hambre-=3
        self.felicidad+=1
        self.energia-=1
        self.acciones+=1

    #dormir() → aumenta energía en 4 y felicidad en 1.  imprime: está durmiendo 😴
    def dormir(self):
        print(f"\n{self.nombre} está durmiendo 😴")
        self.felicidad+=1
        self.energia+=4
        self.acciones+=1

    #jugar() → aumenta felicidad en 2, reduce energía en 2 y aumenta hambre en 1. imprime: está jugando 🎾
    def jugar(self):
        print(f"\n{self.nombre} está jugando 🎾")
        self.felicidad+=2
        self.energia-=2
        self.hambre+=1
        self.acciones+=1

    #aburrirse() → reduce felicidad en 2 (evento aleatorio). imprime: se aburre... 💤"
    def aburrirse(self):
        print(f"\n{self.nombre} se aburre... 💤")
        self.felicidad-=2
        self.acciones+=1  #Extra para dar dificultad

#Caso de uso:
#a. Crear mi Tamagochi y declarar variables
miTamagochi = Tamagochi()
accionesMax = random.randint(5,10)  #Número aleatorio de acciones (5–10) → muere de “vejez”. (mínimo 5, máximo 10)
 
#b. Pedir el nombre de la mascota con input().
miTamagochi.nombrarTamagochi() 

#c. Determinar si Tamagochi Vivo
tamagochiAlive = True

#Bucle Principal
while (tamagochiAlive):
    
    miTamagochi.mostrar_estado() #Mostrar Estado.
   
    accionRealizar = input("¿Que quieres hacer: comer, dormir o jugar? ") #Preguntar acción: comer, dormir, jugar.

    if accionRealizar == "comer":
        miTamagochi.comer()
    elif accionRealizar == "dormir":
        miTamagochi.dormir()
    elif accionRealizar == "jugar":
        miTamagochi.jugar()
    else:
        print(f"Te has equivocado de acción y has perdido turno...")  #Extra para dar dificultad
        miTamagochi.aburrirse()

    time.sleep(1.5)

    if (random.randint(1,5) == 2):
        miTamagochi.aburrirse()
    
    time.sleep(1.5)

#    Limitar valores de variables con min() y max().
#      max hambre: 10
#      max felicidad: 10
#      min energía: 0
    
    miTamagochi.hambre = max(0, miTamagochi.hambre)      # Si el valor de hambre baja de 0, saca 0
    miTamagochi.hambre = min(10, miTamagochi.hambre)     # Si el valor de hambre supera 10, saca 10

    miTamagochi.felicidad = max(0, miTamagochi.felicidad)   # Si el valor de felicidad baja de 0, saca 0
    miTamagochi.felicidad = min(10, miTamagochi.felicidad)  # Si el valor de felicidad supera 10, saca 10

    miTamagochi.energia = max(0, miTamagochi.energia)     # Si el valor de energia baja de 0, saca 0
    miTamagochi.energia = min(10, miTamagochi.energia)    # Si el valor de energia supera 10, saca 10

    #Terminar el juego si: 
    #hambre >= 10 → muere de hambre.
    #energia <= 0 → muere de cansancio.
    if (miTamagochi.hambre >= 10 or miTamagochi.energia <= 0 or miTamagochi.acciones >= accionesMax):
       tamagochiAlive = False       

miTamagochi.mostrar_estado()
if (miTamagochi.hambre == 10):
    print(f"{miTamagochi.nombre} ha muerto de hambre 🪦")
elif (miTamagochi.felicidad == 0):
    print(f"{miTamagochi.nombre} ha muerto de tristeza 🪦")
elif (miTamagochi.energia == 0):
    print(f"{miTamagochi.nombre} ha muerto de cansancio 🪦")
else:
    print(f"{miTamagochi.nombre} ha muerto de viejecito 🪦")

import random
numero = random.randint(1,100)
condicion = False

def pan(panes):
    harina = panes * 62.5
    aceite = panes * 3.75
    azucar = panes * 3.75
    sal = panes * 1.25
    levadura = panes * 1.25
    agua = panes * 43.75
    print("Para hacer ", int(panes), "panes, necesitaras los siguientes ingredientes:")
    print("Harina:", (harina), "gr de harina")
    print("Agua:", (agua), "ml de agua")
    print("Sal:", (sal), "gr de sal")
    print("Levadura:", (levadura), "gr de levadura")
    print("Azucar:", (azucar), "gr de azucar")
    print("Aceite:", (aceite), "ml de aceite")
while condicion == False:
    print("Tu número de la suerte del dia es", (numero))
    print("#######################################################")
    print("# PANCULATOR 2.0 Calculadora de Ingredientes para pan #")
    print("#         Desarrollada en Python por Cronos           #")
    print("#######################################################")
    print(" Por favor ingrese la cantidad de panes que desea elaborar: \n")
    pan(float(input()))
    print("Que deseas hacer? (Escriba salir para terminar el programa")
    opcion = input()
    if opcion == "salir":
        break






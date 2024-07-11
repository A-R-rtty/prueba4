import random, csv, os, msvcrt, time

from funciones import *

while True:
    os.system('cls')
    print("---BIENVENIDO AL P.D.S (PROTOTIPO DE SUELDOS)---")
    print("\n1. Asignar Sueldos Aleatorios.\n2. Clasificar Sueldos.\n3. Ver Estadisticas.\n4. Reporte De Sueldos.\n5. Salir Del Programa.")

    opc = int(input("Ingrese Una Opción: "))

    if opc==1:
        asignar_sueldo()
    
    elif opc==2:
        clasificar_sueldos()

    elif opc==3:
        ver_estadisticas()

    elif opc==4:
        reporte_sueldos()

    elif opc==5:
        salir()

    else:
        os.system('cls')
        print("ERROR! DEBE SELECCIONAR UNA OPCIÓN VALIDA!")
        time.sleep(2)
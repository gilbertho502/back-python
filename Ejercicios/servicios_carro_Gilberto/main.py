from servicios import *

while True:
    print(" ")
    print("Servicios: ")
    print("1. Lavado")
    print("2. Alquiler")
    print("3. Estacionamiento")
    menu = int(input("Seleccione una opcion: "))
    if menu == 1:
        lavar()
    elif menu == 2:
        alquilar()
    elif menu == 3:
        estacionar()
    else:
        print("Opcion no valida")
    

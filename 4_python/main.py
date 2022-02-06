from calculadora import *

# print(suma(1,2))
# print(resta(4,2))

# print(multiplicar(2,2))
# print(dividir(5,2))

while True:
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    menu = "Ingrese la operacion: \n 1. suma \n 2. resta \n 3.Mult \n 4. Division \n 5 Salir : \n"
    opcion = input(menu)
    if opcion == "1": 
        print(suma(a,b))
    elif opcion == "2":
        print(resta(a,b))
    elif opcion == "3":
        print(multiplicar(a,b))
    elif opcion == "4":
        print(dividir(a,b))
    elif opcion =="5":
        print("Adios")
        break
    else:
        print("la opreacion no es valida")
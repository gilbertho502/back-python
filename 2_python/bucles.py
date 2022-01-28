"""
for: cuando se conoco el numero de veces que se repetira el bucle
while: cuando el bucle termina cuando sucede un valor True
"""

# for num in range(1,10,3):
#     print(num)

#Acumuladores y contadores:
contador = 0
acumulador = 0
# for x in range(1,6):
#     sueldo = float(input(f"Ingrese sueldo {x}: "))
#     contador +=1
#     acumulador = acumulador + sueldo
#     promedio_sueldo = acumulador/contador
# print(f"Cantidad de empleados procesados {contador}")
# print(f"El total de la planilla es {acumulador}")
# print(f"El promedio de sueldo es: {promedio_sueldo}")
# print("Fin del bucle")

#Break es salir del bucle
#Continue es seguir la seecuencia del bucle

# for i in range(1,10):
#     if i ==1:
#         break
#     else:
#         print(i) 
#         continue

i = 0
suma = 0

while i<=99:
    i +=1
    suma = suma + i 
    #print(i)
print(f"La suma de los numeros es: {suma}")


#Escribir un programa que nos solicite la contraseña para ingresar al sistema
#si la contraseña es errada debera volver a intentarlo "n" veces

# contador = 0
# constrasena = "python"
# usuario = input("Nombre de usuario: ")
# while True:
#     contra = input("Ingrese la contraseña: ")
#     if contra == constrasena:
#         print(f"bienvenido al sistema {usuario}")
#         break
#     else:
#         contador = contador +1
#         print(f"contraseña incorecta, vuelve a internarlo {contador}")
#         if contador ==3:
#             print("Supero los intentos, se bloqueara el acceso")
#             break


import random

numero_secreto = random.randint(1,100)
intentos = 0
while True:
    numero = int(input("Cual es el numero secreto?: "))
    intentos +=1
    if numero == numero_secreto:
        print("Acertate!!!")
        print(f"Numero de intentos: {intentos}")
        break
    else:
        if numero_secreto > numero:
            print(f"El numero secreto es mayor que {numero}")
        else:
            print(f"El numero secreto es menor que {numero}")


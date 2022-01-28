# contador = 0
# cant_notas_mayores = 0
# cant_notas_menores = 0
# while contador <10:
#     notas = int(input("Ingresa 10 notas de los alumnos: "))
      
#     if notas >= 17:
#         cant_notas_mayores = cant_notas_mayores +1

#     else:
#         cant_notas_menores = cant_notas_menores +1
       
#     contador +=1
# print(f"Cantidad de notas mayores a 17: {cant_notas_mayores}")
# print(f"Cantidad de notas menores a 17: {cant_notas_menores}")


#Ejercicio 2

#producto = input("Que producto desea?: ")

sumtotal=0
while True:
    precio = float(input("Precio del producto?: "))
    cantidad = int(input("Cantidad del producto?: "))
    subtotal = precio * cantidad
    print(f"El total a pagar es: {precio * cantidad}")
    sumtotal =sumtotal+ subtotal
    msj = input("desea seguir comprando? (s/n) ")
    if msj.upper() =="N":
        print(f"total a pagar: {sumtotal}")
        break

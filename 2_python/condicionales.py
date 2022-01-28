"""
Ejercicio 1
"""

# sueldo = float(input("ingrese su sueldo: $"))

# if sueldo <8000: 
#     aumento = 8000*0.12
# else :
#     aumento = sueldo*0.08

# nuevo_sueldo = sueldo + aumento
# print(f"Aumento= ${aumento:.2f} y nuevo sueldo = ${nuevo_sueldo:.2f}")

"""
Ejercicio 2
"""
codigo = input("Ingrese el codigo del empleado: ")
categorias= int(input("Ingrese la categoria: "))
antiguedad= int(input("Ingrese la antiguedad: "))
#flag = bandera
respuesta = False

if categorias == 3 or categorias == 5 :
    if antiguedad >= 5:
        respuesta = True
elif categorias == 2 and antiguedad >= 10:
    respuesta = True
if respuesta:
    resultado = "Reune las caracteristicas para el puesto"
else:
    resultado = "No reune las caracteristicas para el puesto"

print(f"El empleado con codigo {codigo} " + resultado)
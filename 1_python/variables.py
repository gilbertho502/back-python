from os import sep


print("hola mundo desde VSC")

"""
Doc String
Comentario en varias lineas

"""
#reglas para definir varialbles:
#snake_case

edad_persona =28 #tipo int
nombre ="gilberto" #tipo str
precio = 28.8 #tipo float
estado= True #tipo bool

#print(type(edad_persona))
#print(type(nombre))
#print(type(precio))
#print(type(estado))

#colecciones
lista_cursos = ["python", "flask", "django"] #lista (Si se puede modificar )
sueldo = (1900,1700,1850) # tuplas: son inmutables (No se puede modificar)
empleados= {"codigo":"a100", "codigo":"a200"} #diccionario (Si se puede modifica)
#print(type(lista_cursos))
#print(type(sueldo))
#print(type(empleados))

#Palabras reservadas
#import keyword
#print(keyword.kwlist)

#Conversion de datos

valor = "234"
valor2 = 100
valor3= 345.78


# print(type(int(valor)))
# print(type(float(valor2)))
# print(type(str(valor3)))

#Ejercicio Practicos
#Calcular el peso de un objeto

masa = 75
gravedad = 9.81
peso = masa*gravedad
print(peso)

#Promedio de notas
# nom_alumno = input("ingrese el nombre de un alumno: ")
# nota_uno = float(input("Ingrese nota 1: "))
# nota_dos = float(input("Ingrese nota 2: "))
# promedio = (nota_uno + nota_dos)/2
# print(promedio)

#concatenacion
# print("el promedio es: " + str(promedio))
# print("el promedio es: ", promedio)
# print("el promedio del alumno {} es {}". format(nom_alumno, promedio))

#Operadores matematicos
operacion = 5/3
print("El valor formateado es: %.2f" %operacion)

#Operadores logicos

#Ejercicio format
pago_hora = 60.00
# nom_emp= input("Ingrese el nombre del emmpleado: ")
# horas_trab = int(input("Ingrese las horas trabajadas: "))
# pago_jornal = horas_trab*pago_hora
# print("{} Recibira el monto de Q{}".format(nom_emp, pago_jornal))

#----------------------------------------------------------------------

# pizza = int(input("Hola, cuantas rebanadas de pizza trajiste?"))
# comidas = int(input("Cuantas rebanadas se comieron??"))

# print(f"Si trajiste {pizza} rebanadas y se comieron {comidas}, quedan {pizza - comidas} rebanadas")

#Separadores, tabuladores y saltos de linea

print("hola", "mundo", sep="<->")
print("hola", end="")
print("mundo")
#saltos de linea
print("saltos de linea. Viene un salto \n\n")
print("\t tabulador \n\n")
print("comillas .comillas dentro: \"hola\" ")


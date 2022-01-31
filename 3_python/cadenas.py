una_cadena = " Esta es una cadena de texto "
otra_cadena = 'Esta es otra cadena de texto' 

"""
Comentario en 
multiple linea
Doc string
"""
#comentario de una sola linea

print(una_cadena[2]) #Imprimir posicion de una cadena
print(una_cadena[5])
print(una_cadena[6:15]) #Imprimir un rando de caracteres
print(una_cadena[-5:-2]) #substraer caracteres de derecha a izquierda
print(len(una_cadena)) #cantidad de caracteres
print(una_cadena.strip()) #Elimina los espacio en blanco al inicio y final
print(una_cadena.lower()) #todo minuscula
print(una_cadena.upper()) #todo mayuscula
cadena = "PYTHON es un lenguaje interpretado y muy facil de aprender"
print(cadena.replace("PYTHON", "JavaScript")) #Reemplaza cadena de texto
cadena1 = "Python, es muy interesante, lo voy a manejar"
cadena2 = cadena1.split(",") #separa el string en lista
print(cadena2[2])
mensaje = "python maneja diferentes funciones de cadena python"
print(mensaje.capitalize())
print(mensaje.count("python")) #cuenta la cantidad de palabrass
habilidades = "Los lenguajes que mas he aprendido son javascript  y python"
print(habilidades.find("javascript")) #busqueda de cadenas

#Metodos para verificar elementos de una cadena

precio = "23"
if precio.isdigit():
    print("La cadena tiene numeros en su contenido")
else:
    print("La cadena no contiene numeros")
#Creando funcion
def saludar():
    print("Hola esto es una funcion")
    
def funcion_parametros(a,b):
    print(f"Este es el vamor de A: {a} y el valor de B: {b}")

#funcion con valores por defecto
def mensaje(nombre, mensaje="hola"):
    saludo = mensaje + " " + nombre
    print(saludo)
    
    
#funcion con valores indefinidos(listas)
def saluda(*nombres):
    for item in nombres:
        print(item)

#funcion con diccionarios
def elementos(**params):
    for key in params:
        print(key, params[key]) #clave y parametros de la clave 
        
        

#Invocando funciones
#saludar()
#Pasando parametros
#funcion_parametros(12,34)
#mensaje("misra")

#saluda("python", "javascript", "flask","django", "css", "html")

elementos(ciudad = "Tijuana", pais="Mexico")

"""
Manejos de colecciones
listas[]
diccionarios {}
tuplas () Inmutables
"""
cargamos = ["Marias", "Lourdes", "Nicolle", "Alicia", "Armando"]
valores = ["Maria", 20.30, 23, True, (16,24,34),[12,13,43]]

#metodos para listas
#Recorrer elementos de una lista
for item in cargamos:
    print(item)

#Mostar un valor de la lista
print("\n", cargamos[2])
# cargamos.append("Jesus")
# cargamos.append("Jose") #Inserta valores al final de la lista
# cargamos.insert(1,"Alfredo") #Inserta un valor en una posicion dada
# print(cargamos)
# cargamos.pop() #Eliminia el ultimo elementos
# cargamos.pop(3)  #Elimina la posicion dada
# cargamos.remove("Marias") #Elimina por su nombre
# print(cargamos)
# del cargamos[2] #Elimia elemento de la lista por posicion
# cargamos[2] = "Alfredo" #Modifica un elemento de la lista

print("\n", cargamos)

cargamos.sort() #ordena alfabeticamente de forma ascendente
print(cargamos)
cargamos.sort(reverse=True) #ordena la lista de forma descendente
print(cargamos)

cargamos.clear() #limpia selementos de la lista
print(cargamos)
cargamos = [] #inicializar la lista
cargamos = list()


#Realizar un programa que me permita añadir 5 elemetos a una lista

# cursos = []
# for item in range (1,6):
#     nuevo_curso = input(f"Ingrese el curso {item}: ")
#     cursos.append(nuevo_curso)
# print("Mostrando elementos de la lista")
# print(cursos)


#Crear una lista de invitados para la fiesta de armando
#Requisito: traer regalo
lista_invitados = []
msg = ""
while True:
    invitado = input("Ingresa el nombre del invitado: ")
    regalo = input("Ha traido regalo?? S/N ")
    if regalo.upper()=="S":
        lista_invitados.append(invitado)
    msg = input("Desea agregar otro invitado? S/N ")
    if msg.upper() == "N":
        break
print("Lista de invitados")
print(f"Lista de invitados {lista_invitados}")
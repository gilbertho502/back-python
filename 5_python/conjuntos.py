frutas = {"manzanas", "fresas" ,"cerezas"}
frutas.add("platanos")
print(frutas)
#todo adicionar
frutas.update(["naranjas","sandia", "coco"])
#print(frutas)

#remover valores del set

frutas.remove("coco")
# print(frutas)

#tratar de modificar un valor del set
#frutas[0] = "maracuya"

#no permite elementos duplicados
frutas.add("platanos")
print(frutas)
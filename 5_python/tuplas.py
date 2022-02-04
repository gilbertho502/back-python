#las tuplas son inmutables, no se pueden modificar
precios = (100,200,300)
valores = 1,2,3,4,5,6,7


print(type(precios))
print(type(valores))

frutas = "manzanas", "uvas", "fresas"
buscar = input("Ingresa la fruta a buscar: ")
if buscar in frutas:
    print("Si se encuentra la fruta")
else:
    print("Fruta  no encontrada")
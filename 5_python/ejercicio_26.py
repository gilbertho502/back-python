discos = [
    {"genero":"salsa","precio": 56},
    {"genero":"rock","precio": 63},
    {"genero":"pop","precio": 87},
    {"genero":"folclore","precio": 120.50},
]

genero = input("Ingrese el genero ")
cant_discos= int(input("Cuantos discos desea llevar? "))
precio = 0
descuento = 0
for item in discos:
    if item["genero"] == genero:
        if cant_discos  <= 3:
            descuento = 0
            precio =  (cant_discos * item["precio"])
        elif cant_discos == 4:
            precio = cant_discos*(item["precio"] - 0.06*item["precio"])
            descuento = cant_discos * 0.06* item["precio"]
        elif cant_discos <= 10:
            precio =  cant_discos* (item["precio"] - 0.08*item["precio"])
            descuento = cant_discos * 0.08* item["precio"]
        elif cant_discos >10 :
            precio =  cant_discos*( item["precio"] - 0.102*item["precio"])
            descuento = cant_discos * 0.102* item["precio"]
        else:
            print("No se seleccionaron productos")
        if  cant_discos >6 and (genero == "rock" or genero == "pop"):
            print("Se ha ganado un poster")
        else:
            print("Ninguno")
        
    
print(f"El precio total es: {precio:.2f}")
print(f"El descuento para la compra es de {descuento:.2f}")
def lavar():
    print("Rapido o profundo??")
    iva = 0.12
    rap = 5
    prof = 10
    total = 0
    opcion = input("Seleccione el tipo de lavado?: ")
    if opcion == "rapido":
        total = (iva * rap) +rap
    elif opcion == "profundo":
        total = (iva * prof) + prof
    else:
        print("No es una opcion valida")
    print(f"El total a pagar es ${total:.2f} ")
       
       
def alquilar():
    auto = input("Seleccione el tipo de auto a alquilar: A/B/C ")
    dias = int(input("Dias para alquilar?: "))
    precio_dia = 0
    precio_total = 0
    if auto.upper() == "A":
        precio_dia = 100 * dias
    elif auto.upper() == "B":
        precio_dia = 150 * dias
    elif auto.upper() == "C":
        precio_dia = 200 * dias
    else:
        print("Tipo de auto no valido")
    precio_total = precio_dia + (precio_dia * 0.12)
    print(f"Total a pagar es de: ${precio_total}")

def estacionar():
    hora = float(input("Tiempo de parqueo? "))
    precio = 0
    precio_total = 0
    iva = 0.12
    extra = 0 
    adicional = 0.50
    if hora <= 3:
        precio = 2
    elif hora >3 and hora <24:
        extra = hora -3 
        precio = (extra * adicional)+2
    elif hora <=24:
        precio = 10
    else: 
        print("Hora no disponible")
    precio_total = precio + (precio * iva)
    print(f"El precio total de parqueo es: {precio_total}")
    
#alquilar()
#lavar()
#estacionar()
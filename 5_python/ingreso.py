"""
para ingresar a ver el partido entre Peru y Ecuador
se tien que cumplir los siguientes requisitos:
que el hincha sea mayor de edad
Tener las 3 dosis de vacuna
Si cumple con esas condiciones se le asignara un asiento,
no se le puede asignar un asiente repetido y al final mostrar
los numeros de asientos y personas.

"""

hinchas = [
    {"dni": "10210902", "nombre": "Armando", "nac": 1975, "dosis": 3, "asieto": ""},
    {"dni": "10210903", "nombre": "Diego", "nac": 2017, "dosis": 2, "asieto": ""},
    {"dni": "10210904", "nombre": "Gilberto", "nac": 2000, "dosis": 1, "asieto": ""},   
]

# encontrar = False
resp = ""
año_actual = 2022
while resp!= "N":
    dni = input("Ingrese el DNI: ")
    for item in  hinchas:
        if (dni in item["dni"]):
            edad = año_actual - item["nac"]
            if edad >= 18 and 3 == item["dosis"]:
                asiento = input("Asignar un numero de asiento: ")
                item["asiento"] = asiento
                print(f"Se le asigno el asiento {asiento} al hincha")
            else:
                print("El hicha no cumple con algunas condiciones")
                break
            resp = input("Desea continuar <S/N>")
            if resp == "N":
                break
print(hinchas)
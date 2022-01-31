sueldos = {
    "epm001": 1200,
    "emp002": 1800,
    "emp003": 1900
}

print(sueldos)
print(sueldos["emp003"])

#Actualizar el valor del diccionario
sueldos["emp002"] = 2800
print(sueldos)
sueldos.update({"emp002":3700})
print(sueldos)

#Eliminar un elementos del diccionario:
del sueldos ["emp003"]
print(sueldos)

#Insertar elementos al diccionaio
sueldos["emp003"] = 7600
sueldos["emp004"] = 760
print(sueldos)

#Crud
#Create = crear
#Read = leer
#Update = actualizar
#Delete = eliminar

#Recorrer el diccionario
for item in sueldos.keys():
    print(item)

"""
Realizar u programa que simule la consulta de un cajero de banco.
se debe tener un origen de datos con 5 clientes.
El cajero debera solicitar numero de cuentas y le
mostrara su saldo.
"""

clientes = [
    {"cuentas": "2334455", "apellido": "ruiz", "nombre": "armando", "saldo": 7000},
    {"cuentas": "2334456", "apellido": "gomez", "nombre": "pedro", "saldo": 8800},
    {"cuentas": "2334457", "apellido": "cespedes", "nombre": "javier", "saldo": 9000},
    {"cuentas": "2334458", "apellido": "linares", "nombre": "oscar", "saldo": 12000},
    {"cuentas": "2334459", "apellido": "palomino", "nombre": "maria", "saldo": 17000},
    
]
cuenta = input ("Engrese su numero de cuenta a consultar: ")
for item in clientes:
    if cuenta ==item["cuentas"]:
        print(f"El saldo actual es: {item['saldo']}")
        break

        

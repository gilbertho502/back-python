from base_de_datos import empleados

""" 
Indicaciones:
1) Buscar un empleado por codigo y mostrar el sueldo que gana
2) Sumar el sueldo de todo un area
"""

def buscar_empleado(bd):
    existe = False
    cod_empl = input("Ingrese el codigo del empleado: ")
    for item in bd:
        if cod_empl == item['codigo']:
            print(f"El sueldo del empleado {item['nombre']} {item['apellido']} es: {item['sueldo']}")
            existe = True
            break
    if existe == False:
        print("El empleado no existe")
            
def sumar_sueldos(bd):
    existe =False
    sueldo_tot = 0
    area = input("Ingrese el area de trabajo: ")
    for item in bd:
        if area == item['area']:
            sueldo_tot = sueldo_tot + item['sueldo']
            existe = True
    if existe == False:
        print("El area no existe")
    print(f"El sueldo total del area es: {sueldo_tot}")                 
# buscar_empleado(empleados)
sumar_sueldos(empleados)
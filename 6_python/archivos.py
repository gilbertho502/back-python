"""
CSV valores separados por coma.
Es un formato de archivo simple que se utiliza para almacenar datos 
tabulares, como una hoja de calculo o una BD.
Es un formato muy comun para Data Sciencie
"""

import csv
from multiprocessing.sharedctypes import Value
#abre el archivo en la variable asiganada "data_cargamos"
def data_alumnos_csv():
    with open('cargamos.csv', 'r') as data_cargamos:
        #csv_leer = csv.reader(data_cargamos, delimiter=";")
        #leer el archivo linea por linea
        csv_leer = csv.reader(data_cargamos)
        #convirtiendo el archivo a una coleccion del tipo list
        lista_estudiantes = list(csv_leer)
        return lista_estudiantes

data_alumnos_csv()

def cursos_alumn(estudiantes,curso_param):
    estudiantes_curso = []
    for CODIGO,NOMBRE,APELLIDOS,CURSO,P1,P2,P3,PRO in estudiantes:
        if CURSO == curso_param:
            estudiantes_curso.append((NOMBRE,CURSO))
    return estudiantes_curso

# curso = input("Ingrese el curso a mostrar sus estudiantes: ")
# print(cursos_alumn(data_alumnos_csv(), curso))

#VISUALIZAR EL NOMBRE Y APELLIDO DEL ALUMNO
#QUE SACO LA NOTA MAS ALTA DEL CURSO

def nota_mayor_curso(estudiantes):
    con = 0
    nota_mayor = 0.0
    prom_alum = 0
    for CODIGO,NOMBRE,APELLIDOS,CURSO,P1,P2,P3,PRO in estudiantes:
        if con > 0:
            prom_alum = float(PRO)
            if float(prom_alum) >= float(nota_mayor):
                nota_mayor = PRO 
        con = con+1
    return nota_mayor
print(nota_mayor_curso(data_alumnos_csv()))

# link clase: 
# https://us02web.zoom.us/j/85376584368?pwd=bzZOM2ptVzB3YnU5OVlnWjJpSGRVQT09#success
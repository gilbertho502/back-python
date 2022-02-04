"""
Crear un programa con POO.
Que  permita listar los productos que estan suspendidos
Crear los atributos deacuerdo a los campos del excel,
hacer un metodo quenos permitar cargar la informacion del csv

"""
import csv
from datetime import date

class productos:
    #atributos
    def __init__(self,IdProducto,NombreProducto,Proveedor,Categoria,CantidadPorUnidad,PrecioUnidad,UnidadesEnExistencia,UnidadesEnPedido,NivelNuevoPedido,Suspendido ):
        self.IdProducto = IdProducto
        self.NombreProduco = NombreProducto
        self.Proveedor = Proveedor
        self.Categoria = Categoria
        self.CantidadPorUnidad = CantidadPorUnidad
        self.PrecioUnidad = PrecioUnidad
        self.UnidadesEnExistencia = UnidadesEnExistencia
        self.UnidadesEnPedido = UnidadesEnPedido
        self.NivelNuevoPedido = NivelNuevoPedido
        self.Suspendido = Suspendido
        self.productos= []

    #metodos
    def data_productos_csv(self):
        with open('productos.csv', 'r') as data_productos:
            #csv_leer = csv.reader(data_cargamos, delimiter=";")
            csv_leer = csv.reader(data_productos)
            lista_producots = list(csv_leer)
            return lista_producots
    def mostrar_suspendidos(self, product, data):
        producto_sus = []
        for self.IdProducto,NombreProducto,Proveedor,Categoria,CantidadPorUnidad,PrecioUnidad,UnidadesEnExistencia,UnidadesEnPedido,NivelNuevoPedido,self.Suspendido in product:
            if date == "FALSO":
                producto_sus.append((date))
            return producto_sus


producto1 = productos(78, "arroz","misra","granos",1,2,5,3,19,"Verdadero")

print(producto1.data_productos_csv())
print(producto1.mostrar_suspendidos(data_productos_csv()))
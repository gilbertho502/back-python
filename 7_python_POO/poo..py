class persona:
    pass

#creando los objetos

#crear el objeto = instanciar el objeto
pedro = persona()
cristina = persona()
manuel = persona()
maria = persona()

#/////////////////////////////////////////////////////////////////////////////////

class animal:
    #atributos
    def __init__(self, nombre, edad):
        self.nom = nombre
        self.ed = edad
    #metodos
    def comer(self):
        if self.ed >10:
            print(f"El animal {self.nom} debe comer muy poco")
        else:
            print(f"Debes alimentar mas a tu mascota {self.nom}")
  
#objetos
perro = animal("pancho", 4)
gato = animal("paco", 11)
raton = animal("isijara", 30)

#metodos
perro.comer()
gato.comer()
raton.comer()

# print(perro.nom)
# print(perro.ed)
# print(gato.nom)

#muestra los atributos del objeto crado como un diccionario
print(perro.__dict__)
print(gato.__dict__)
# reakuza un rorama que muesstre la informacion 
# dek cabdudati a evakuar en su nuevo puesto

class candidato:
    #atributos
    def __init__(self, apellido="Vicente", nombre = "Gilberto", edad= 26, pais = "Guatemala", ciudad="Guatemala"):
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.ciudad = ciudad
        self.habilidades = []

    #metodos
    def candi_info(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} años y es de {self.pais} de la ciudad {self.ciudad}"
    def add_habildad(self, habilidades):
        self.habilidades.append(habilidades)


#objetos

candidato1 = candidato()
candidato2 = candidato("gonzales","pedro",34, "Mexico", "Mexico")
candidato3 = candidato("ramos", "jose", 29, "mexico", "df")
#usando el metodo
candidato3.add_habildad("python")
candidato3.add_habildad("flask")
candidato3.add_habildad("django")

print(candidato1.candi_info())
print(candidato2.candi_info())
print(candidato3.habilidades)
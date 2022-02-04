
class peliculas:
    #atributos
    def __init__(self, nombre, duracion, idioma, año):
        self.nombre = nombre
        self.duracion = duracion
        self.idioma = idioma
        self.año = año
    #el metodo str permite visualizar su contenido cuando se llama al objeto
    def __str__(self):
        return f"{self.nombre} {self.duracion}"

    def iniciar_peli(self, play):
        if play == True:
            print(f"La pelicula {self.nombre} ha iniciado!!")
        else:
            print("La pelicula no se ha iniciado")

    def pausar(self, pausa):
        if pausa == True:
            print(f"La pelicula {self.nombre} se ha pausado")
        else:
            print("La pelicula continua")

#Herencia entre padres
#clase hija: comedia,  clase padres: peliculas.
class comedia(peliculas):
    def __init__(self, nombre, duracion, idioma, año, pais):
        super().__init__(nombre, duracion, idioma, año)
        self.pais = pais
    #metodos
    def subtitulos(self, sub):
        if sub == True:
            print(f"La pelicula {self.nombre} tiene subtitulos")
        else:
            print(f"La pelicula {self.nombre} no tiene subtitulos")


pelicula1 = peliculas("scary movie", 90, "ingles", 2000)
pelicula1.iniciar_peli(True)
pelicula1.pausar(True)
# print(pelicula1)
# print(pelicula1.__dict__)

pelicula2 = comedia("End Game", 180, "español", 2019, "usa" )
print(pelicula2.__dict__)
pelicula2.subtitulos(True)
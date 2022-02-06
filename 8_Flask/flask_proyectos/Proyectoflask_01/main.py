from flask import Flask, render_template

#Creando el proyecto
app = Flask(__name__) 

data_cargamos= [
    {"nombre":"Alicia", "Apellido":"Guerrero", "picture": "https://picsum.photos/200/300?random=1"},
    {"nombre":"Carlos", "Apellido":"Aguilar", "picture": "https://picsum.photos/200/300?random=2"},
    {"nombre":"Diego", "Apellido":"Santizo", "picture": "https://picsum.photos/200/300?random=3"},
    {"nombre":"Cecilia", "Apellido":"Alonzo", "picture": "https://picsum.photos/200/300?random=4"},
    {"nombre":"Javier", "Apellido":"Catalan", "picture": "https://picsum.photos/200/300?random=5"},
]

#Creando la primera ruta
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cargamos")
def cargamos():
    return render_template("cargamos.html", alumnos= data_cargamos)

@app.route("/acercade")
def acercade():
    return render_template("acercade.html")


    
#ejecutando el servidor
app.run( debug=True)
#para cambiar de puerto
#app.run(port= " 5010", debug=True)
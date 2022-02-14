
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cargamos2022@localhost/bdcargamos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#creando el modelo de productos que se convertira en un tabla
#este proceso se llama migracionç

class productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.Text)
    precio = db.Column(db.Integer)
    state = db.Column(db.Boolean, default= True)

#creando objetos de la base de datos
db.create_all()

@app.route("/")
def index():
    productos=productos.query.all()
    template_name = "index.html"
    return render_template(template_name, productos = productos)

app.run(debug=True)
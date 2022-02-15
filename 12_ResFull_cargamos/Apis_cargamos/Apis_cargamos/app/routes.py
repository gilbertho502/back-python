from flask import render_template,make_response,jsonify
from app import app,db
from app.models import Grupos
from app.serializer import grupos_schema

@app.route('/')
def index():
    template_name="index.html"
    grupos=Grupos.query.all()
    return render_template(template_name,grupos=grupos)


#todo crear el endpoint para traer todas los grupos
#todo en formato JSON

@app.route("/listar_grupos",methods=["GET"])
def listar_grupos():
    #todo seleccionado todos los objetos de la clase grupos
    grupos=Grupos.query.all()
    #todo serializando y seleccionado los atributos a cast en json
    result=grupos_schema.dump(grupos)
    
    #todo creando el documento de salida
    data={
        'message':'Todas mis grupos',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))
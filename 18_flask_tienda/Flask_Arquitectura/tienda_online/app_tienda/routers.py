
from unittest import result
from flask import render_template,request, redirect, flash, url_for, make_response, jsonify
from importlib_metadata import method_cache
from app_tienda import app,db
from app_tienda.models import Usuarios
from app_tienda.serializers import user_schema, users_schema
from flask_cors import cross_origin

@app.route('/index')
def index():
    template_name="index.html"
    usuarios=Usuarios.query.all()
    return render_template(template_name,usuarios=usuarios)


@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        passw = request.form['passw']
        login= Usuarios.query.filter_by(username = uname, password = passw).first()
        if login is not None:
            return redirect(url_for('index'))
        else:
            flash("Es incorrecto el usuario o password")
            return redirect(url_for('login'))
    render_template('login.html')

@app.route("/registrar", methods = ['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        new_usuario = Usuarios(cod_usuario=40,username=uname, email=mail, password=passw)
        db.session.add(new_usuario)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registro.html')


#capa de servicios
@cross_origin
@app.route('/autenticar/<uname>/<passw>', methods=["POST"])
def autenticar(uname, passw):
    login=Usuarios.query.filter_by(username = uname, password = passw).first()
    result = users_schema.dump(login)
    if login is not None:
        data = {
            'message':'Bienvenido',
            'status': 200,
            'data' : result
        }
    else:
        data = {
            'message':'Error',
            'status': 400,
        }
    return make_response(jsonify(data))

@cross_origin
@app.route('/add_usuarios', methods=["POST"])
def add_usuarios():
    uname = request.json['uname']
    mail = request.json['mail']
    passw = request.json['passw']
    new_user = Usuarios(cod_usuario=40,username=uname, email=mail, password=passw)
    db.session.add(new_user) #nuevo_usuario
    db.session.commit()
    result= user_schema.dump(new_user)
    data = {
            'message':'Bienvenido',
            'status': 200,
            'data' : result
        }
    return make_response(jsonify(data))

# en mpostregss
# create sequence usuarios_id_seq;
'''
alter table usuarios
alter colum cod_usuario set defaul nextval(usuarios_id_seq)
'''
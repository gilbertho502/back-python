from flask import  Flask
from app_tienda import config
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

#todo creando la aplicacion
app=Flask(__name__)
cors=CORS(app)
app.secrey_key = os.urandom(24)
#todo Conexion con la BD
app.config['CORS_HEADERS']= 'Content-Type'
app.config.from_object(config.Config)
db=SQLAlchemy(app)

from app_tienda import routers,models
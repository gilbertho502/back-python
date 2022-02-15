class Config(object):
    #todo conectado a la base de datos de MYSQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cargamos2022@localhost/bdcargamos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
# Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow
from controlador import *
# Crea una instancia de la clase Flask con el nombre de la aplicación
app = Flask(__name__)
# Configura CORS para permitir el acceso desde el frontend al backend
CORS(app)

'''
En este código, se están configurando la base de datos y se están creando objetos para interactuar con ella utilizando SQLAlchemy y Marshmallow.

app.config["SQLALCHEMY_DATABASE_URI"]: Se configura la URI (Uniform Resource Identifier) de la base de datos. En este caso, se está utilizando MySQL como el motor de base de datos, el usuario y la contraseña son "root", y la base de datos se llama "proyecto". Esta configuración permite establecer la conexión con la base de datos.

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]: Se configura el seguimiento de modificaciones de SQLAlchemy. Al establecerlo en False, se desactiva el seguimiento automático de modificaciones en los objetos SQLAlchemy, lo cual mejora el rendimiento.

db = SQLAlchemy(app): Se crea un objeto db de la clase SQLAlchemy, que se utilizará para interactuar con la base de datos. Este objeto proporciona métodos y funcionalidades para realizar consultas y operaciones en la base de datos.

ma = Marshmallow(app): Se crea un objeto ma de la clase Marshmallow, que se utilizará para serializar y deserializar objetos Python a JSON y viceversa. Marshmallow proporciona una forma sencilla de definir esquemas de datos y validar la entrada y salida de datos en la aplicación. Este objeto se utilizará para definir los esquemas de los modelos de datos en la aplicación.

'''
# Configura la URI de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/proyecto"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://pablo:StR50103@localhost/lanuquitos"
# Configura el seguimiento de modificaciones de SQLAlchemy a False para mejorar el rendimiento
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Crea una instancia de la clase SQLAlchemy y la asigna al objeto db para interactuar con la base de datos
db = SQLAlchemy(app)
# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)


with app.app_context():
    db.create_all() 


'''
lanuquito_schema = LanuquitoSchema()
lanuquitos_schema =LanuquitoSchema(many=True)    
'''
    # Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)

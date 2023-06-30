from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from configDB import SQLALQUEMY_DATABASE_URI
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app=Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALQUEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
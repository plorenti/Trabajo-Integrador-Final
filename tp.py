from configApp import app,db
from controlador import *


with app.app_context():
    db.create_all()

    # Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)

    
from configApp import app, db
from modelos import Lanuquito, Categoria , Imagen, Material, MaterialesLanuquito
from schema import lanuquitos_schema, lanuquito_schema ,categoria_schema, categorias_schema
from schema import  imagen_schema, imagenes_schema, material_schema, materiales_schema
from schema import materialesLanuquito_schema, materialesLanuquitos_schema
from flask import jsonify, request, render_template

@app.route("/test")
def test():
    todos = Lanuquito.query.all()
    resultado = lanuquitos_schema.dump(todos)
    return render_template("index.html" ,lanuquitos=resultado)

#CONTROLADOR LANUQUITOS
@app.route("/lanuquito/<id>", methods=["GET"])
def detalle_Lanuquito(id):
    lanuquito = Lanuquito.query.get(id)
    resultado = lanuquito_schema.dump(lanuquito)
    return render_template("lanuquito.html", lanuquito=resultado)

@app.route("/lanuquitos", methods=["GET"])
def get_Lanuquitos():
    todos = Lanuquito.query.all()
    resultado = lanuquitos_schema.dump(todos)

    return resultado


@app.route("/lanuquitos", methods=["POST"])
def crear_lanuquito():
    nombre=request.json["nombre"]
    precio=request.json["precio"]
    id_categoria = request.json["id_categoria"]
     
    nuevo=Lanuquito(nombre,precio,id_categoria)
    db.session.add(nuevo)
    db.session.commit()
    return lanuquito_schema.jsonify(nuevo)

@app.route("/lanuquitos/<id>", methods=["GET"])
def get_Lanuquito(id):
    lanuquito = Lanuquito.query.get(id)
    return lanuquito_schema.jsonify(lanuquito)

@app.route("/lanuquitos/<id>", methods=["DELETE"])
def borrar_Lanuquito(id):
    lanuquito = Lanuquito.query.get(id)
    session = db.session  
    lanuquito = session.merge(lanuquito)  # Vincula el objeto Lanuquito a la sesión
    lanuquito.categoria  # Accede a la relación "categoria"
    db.session.delete(lanuquito)
    db.session.commit()
    return lanuquito_schema.jsonify(lanuquito)

@app.route("/lanuquitos/<id>",methods=["PUT"])
def actualiza_Lanuquito(id):
    lanuquito = Lanuquito.query.get(id)
    lanuquito.nombre = request.json["nombre"]
    lanuquito.precio = request.json["precio"]
    lanuquito.id_categoria = request.json["id_categoria"]

    db.session.commit()
    return lanuquito_schema.jsonify(lanuquito)

#CONTROLADOR CATEGORIAS
@app.route("/categorias", methods=["GET"])
def get_Categorias():
    todas = Categoria.query.all()
    resultado = categorias_schema.dump(todas)
    return jsonify(resultado)

@app.route("/categorias", methods=["POST"])
def crear_categoria():
    nombre=request.json["nombre"]
    categoria = Categoria(nombre)
    db.session.add(categoria)
    db.session.commit()
    return categoria_schema.jsonify(categoria)

@app.route("/categorias/<id>", methods=["GET"])
def get_Categoria(id):
    todas = Categoria.query.get(id)
    resultado = categoria_schema.dump(todas)
    return jsonify(resultado)

@app.route("/categorias/<id>",methods=["PUT"])
def actualiza_categoria(id):
    categoria = Categoria.query.get(id)
    categoria.nombre = request.json["nombre"]
    db.session.commit()
    return categoria_schema.jsonify(categoria)

@app.route("/categorias/<id>", methods=["DELETE"])
def borrar_categoria(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return categoria_schema.jsonify(categoria)

#CONTROLADOR IMAGENES

@app.route("/imagenes", methods=["POST"])
def nueva_imagen():
    ruta=request.json["ruta"]
    id_lanuquito=request.json["id_lanuquito"]
    imagen = Imagen(ruta,id_lanuquito)
    db.session.add(imagen)
    db.session.commit()
    return imagen_schema.jsonify(imagen)

@app.route("/imagenes",methods=["GET"])
def get_imagenes():
    imagenes = Imagen.query.all()
    resultado = imagenes_schema.dump(imagenes)
    return imagenes_schema.jsonify(resultado)

@app.route("/imagenes/<id>",methods=["PUT"])
def actualiza_imagen(id):
    imagen = Imagen.query.get(id)
    imagen.ruta = request.json["ruta"]
    imagen.id_lanuquito = request.json["id_lanuquito"]
    db.session.commit()
    return imagen_schema.jsonify(imagen)

@app.route("/imagenes/<id>",methods=["DELETE"])
def borrar_imagen(id):
    imagen = Imagen.query.get(id)
    db.session.delete(imagen)
    db.session.commit()
    return imagen_schema.jsonify(imagen)

#CONTROLADOR MATERIAL
@app.route("/materiales", methods=["POST"])
def nuevo_material():
    material=request.json["material"]
    precio=request.json["precio"]
    proveedor=request.json["proveedor"]
    material = Material(material,precio,proveedor)
    db.session.add(material)
    db.session.commit()
    return material_schema.jsonify(material)

@app.route("/materiales",methods=["GET"])
def get_materiales():
    materiales = Material.query.all()
    resultado = materiales_schema.dump(materiales)
    return materiales_schema.jsonify(resultado)

@app.route("/materiales/<id>",methods=["GET"])
def get_material(id):
    materiales = Material.query.get(id)
    resultado = material_schema.dump(materiales)
    return material_schema.jsonify(resultado)

@app.route("/materiales/<id>",methods=["PUT"])
def actualiza_material(id):
    material = Material.query.get(id)
    material.material =request.json["material"]
    material.precio=request.json["precio"]
    material.proveedor=request.json["proveedor"]
    db.session.commit()
    return material_schema.jsonify(material)

@app.route("/materiales/<id>",methods=["DELETE"])
def borrar_material(id):
    material = Material.query.get(id)
    db.session.delete(material)
    db.session.commit()
    return material_schema.jsonify(material)

#CONTROLADOR MATERIALESLANUQUITO
@app.route("/materiales_lanuquitos", methods=["POST"])
def nuevo_material_lanuquito():
    id_lanuquito=request.json["id_lanuquito"]
    id_material=request.json["id_material"]
    cantidad=request.json["cantidad"]
    precio=request.json["precio"]
    material = MaterialesLanuquito(id_lanuquito,id_material,cantidad,precio)
    db.session.add(material)
    db.session.commit()
    return materialesLanuquito_schema.jsonify(material)

@app.route("/materiales_lanuquitos", methods=["GET"])
def get_materiales_lanuquitos():
    todos = MaterialesLanuquito.query.all()
    resultado = materialesLanuquitos_schema.dump(todos)
    return materialesLanuquitos_schema.jsonify(resultado)

@app.route("/materiales_lanuquitos/<id>", methods=["GET"])
def get_material_lanuquito(id):
    material = MaterialesLanuquito.query.get(id)
    resultado = materialesLanuquito_schema.dump(material)

    return materialesLanuquito_schema.jsonify(resultado)

@app.route("/materiales_lanuquito/<id>", methods=["GET"]) #devuelve los materiales por ID de Lanuquito
def get_materiales_lanuquito(id):
    todos = MaterialesLanuquito.query.filter(MaterialesLanuquito.id_lanuquito==id).all()
    resultado = materialesLanuquitos_schema.dump(todos)
    return materialesLanuquitos_schema.jsonify(resultado)

@app.route("/materiales_lanuquitos",methods=["PUT"])
def actualiza_material_lanuquito(id):
    material = MaterialesLanuquito.query.get(id)
    material.id_lanuquito = request.json["id_lanuquito"]
    material.id_material = request.json["id_lanuquito"]
    material.cantidad = request.json["cantidad"]
    material.precio = request.json["precio"]
    db.session.commit()
    return materialesLanuquito_schema.jsonify(material)

@app.route("/materiales_lanuquitos/<id>", methods=["DELETE"])
def borrar_materiales_lanuquito(id):
    material = MaterialesLanuquito.query.get(id)
    db.session.delete(material)
    db.session.commit()
    return materialesLanuquito_schema.jsonify(material)

from configApp import db 

class Imagen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ruta = db.Column(db.String(200)) 
    id_lanuquito = db.Column(db.Integer, db.ForeignKey('lanuquito.id'))
    imagenes =  db.relationship('Lanuquito', back_populates='imagenes',
                                primaryjoin="Lanuquito.id == Imagen.id_lanuquito")
    
    def __init__(self,ruta,id_lanuquito):
        self.ruta=ruta
        self.id_lanuquito=id_lanuquito


class Lanuquito(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))        
    precio = db.Column(db.Double)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    categoria = db.relationship('Categoria', backref='Lanuquito', foreign_keys=[id_categoria])
    imagenes = db.relationship('Imagen', backref='lanuquito')
    materiales = db.relationship('MaterialesLanuquito', backref='lanuquito')

    def __init__(self,nombre,precio,id_categoria):
        self.nombre=nombre
        self.precio=precio
        self.id_categoria=id_categoria

        
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(200))
    precio = db.Column(db.Double)
    proveedor = db.Column(db.String(200))
    materiales =  db.relationship('MaterialesLanuquito', back_populates='materiales',
                                primaryjoin="MaterialesLanuquito.id_material == Material.id")
    
    def __init__(self,material,precio,proveedor):
        self.material=material
        self.precio=precio
        self.proveedor=proveedor

    

class MaterialesLanuquito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_lanuquito = db.Column(db.Integer, db.ForeignKey('lanuquito.id'))
    id_material = db.Column(db.Integer, db.ForeignKey('material.id'))
    materiales = db.relationship('Material', backref='MaterialesLanuquito')
    cantidad = db.Column(db.Double)
    precio = db.Column(db.Double)

    def __init__(self,id_lanuquito,id_material,cantidad,precio):
        self.id_lanuquito=id_lanuquito
        self.id_material=id_material
        self.cantidad=cantidad
        self.precio=precio



class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    
    def __init__(self,nombre):
        self.nombre=nombre


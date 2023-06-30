from configApp import ma

class LanuquitoSchema(ma.Schema):
    '''categoria = ma.Nested('CategoriaSchema')
    imagenes = ma.Nested('ImagenLanuquitoSchema', many=True)
    materiales = ma.Nested('MaterialLanuquitoSchema', many=True)'''
    categoria = ma.Nested('CategoriaLanuquitoSchema')
    imagenes = ma.Nested('ImagenLanuquitoSchema', many=True)
    materiales = ma.Nested('MaterialLanuquitoSchema', many=True)
    class Meta:
        fields = ('id', 'nombre', 'precio','categoria',"imagenes","materiales")


class ImagenSchema(ma.Schema):
    class Meta:
        fields = ('id', 'ruta','id_lanuquito')

class ImagenLanuquitoSchema(ma.Schema):
    class Meta:
        fields = ["ruta"]       

class CategoriaLanuquitoSchema(ma.Schema):
    class Meta:
        fields = ["nombre"]

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')

class MaterialSchema(ma.Schema):
    class Meta:
        fields = ('id', 'material','precio','proveedor')

class MaterialLanuquitoSchema(ma.Schema):
    materiales = ma.Nested('MaterialSchema', many=True)
    class Meta:
        fields = ('id','id_lanuquito' ,'id_material' ,'precio','cantidad')

     


lanuquito_schema= LanuquitoSchema()
lanuquitos_schema = LanuquitoSchema(many=True)        
categoria_schema = CategoriaSchema()
categorias_schema= CategoriaSchema(many=True)
imagen_schema=ImagenSchema()
imagenes_schema=ImagenSchema(many=True)
material_schema=MaterialSchema()
materiales_schema=MaterialSchema(many=True)
materialesLanuquito_schema=MaterialLanuquitoSchema()
materialesLanuquitos_schema=MaterialLanuquitoSchema(many=True)


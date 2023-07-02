var id = location.search.substr(4);
const { createApp } = Vue;

createApp({
    data(){
        return {
            url:"https://plorenti.pythonanywhere.com/lanuquitos/"+id,
            url_categorias:"https://plorenti.pythonanywhere.com/categorias",
            url_materiales:"https://plorenti.pythonanywhere.com/materiales",
            url_materialLanuquito:"https://plorenti.pythonanywhere.com/materiales_lanuquitos",
            lanuquito:[],
            categorias:[],
            id:0,
            nombre:"",
            id_categoria:0,
            precio:0,
            imagenes:[],
            materialesLanuquitos:[],
            materiales_todos:[],
            nuevoMaterial:0,
            nuevoMaterialCantidad:0,
            nuevoMaterialPrecio:0,
            lista_nuevosMateriales:[],
            catSel:0,

        };
    },
    methods:{
        fetchData(url, url_categorias, url_materiales) {

            fetch(url)
              .then((response) => response.json())
              .then((data) => {
                
                this.lanuquito=data;
                this.imagenes = this.lanuquito.imagenes;
                this.materialesLanuquitos=this.lanuquito.materiales;
                this.materiales=this.lanuquito.materiales_todos;

              })
              .catch((err) => {
                console.error(err);
                this.error = true;
              });
               //CARGO CATEGORIAS
               fetch(url_categorias)
               .then((response) => response.json())
               .then((data) => {
                 this.categorias = data;
               })
               .catch((err) => {
                 console.error(err);
                 this.error = true;
               });
              //CARGO MATERIALES
               fetch(url_materiales)
               .then((response) => response.json())
               .then((data) => {
                 this.materiales_todos = data;
               })
               .catch((err) => {
                 console.error(err);
                 this.error = true;
               });
            },
            agregarMaterialLanuquito(){
                let material = {
                    id_lanuquito: this.lanuquito.id,
                    id_material: this.nuevoMaterial,
                    cantidad:this.nuevoMaterialCantidad,
                    precio:this.nuevoMaterialPrecio,
    
                 }
                 this.materialesLanuquitos.push(material)
                 this.lista_nuevosMateriales.push(material)
            },
            agregarMaterial(material){
             console.log(this.nuevoMaterial)
             console.log(this.lanuquito.id)
             console.log(this.nuevoMaterialCantidad)
             console.log(this.nuevoMaterialPrecio)
           
           

                         //Configurar fetch
            let opciones = {
                body: JSON.stringify(material), // Convertir el objeto a una cadena JSON
                method: "POST", // Establecer el método HTTP como POST
                headers: { "Content-Type": "application/json" },
                redirect: "follow",
              };  
       
              //Ejecutar
              fetch(this.url_materialLanuquito, opciones)
              .then(() =>{
                alert("Material Agregado!");
                this.fetchData(this.url,this.url_categorias);
                $('#agregar-material-modal').modal('hide');
              })
              .catch((err) => {
                console.error(err);
                alert("Error al Grabar.");
              });


            },
            eliminarMaterial(){
                
            },
            actualizar(){
                console.log(this.lista_nuevosMateriales)
                this.lista_nuevosMateriales.forEach(material => {
                    console.log(material)
                    this.agregarMaterial(material);
                });
            }
          },
  created() {

    this.fetchData(this.url, this.url_categorias,this.url_materiales);
   
  },


}).mount("#app");
import web
from mvc.models.model_contactos import ModelContactos


render = web.template.render('mvc/views', base='template')


class InsertarContacto:


    # Permite mostrar la pagina (¡ambas letras en mayúscula!)
    def GET(self):
        return render.insertar_contacto() #type: ignore


    # Recibe los inputs del formulario y accede a cada uno
    def POST(self):
        # Accede a los datos del formulario 'contactos'
        formulario = web.input()
        
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']


        model_contactos = ModelContactos()
        datos = model_contactos.insertarContacto(nombre, email, telefono)


        html = """
        <h1>Contacto almacenado correctamente</h1>
        <a href='/contactos'>Regresar</a>
        """
        return html

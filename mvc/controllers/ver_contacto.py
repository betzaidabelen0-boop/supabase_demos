import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')


class VerContacto:

    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContactoPorId(id_contacto)
        print(contacto)
        return render.ver_contacto(contacto)

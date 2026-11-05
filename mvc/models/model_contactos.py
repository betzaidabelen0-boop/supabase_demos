import os
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

class ModelContactos:

    def __init__(self):
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", ""),
            )
        except Exception as error:
            print(
                f"ERROR 100: {error.args[0] if error.args else 'Error al conectar'}"
            )

    def obtenerContactos(self):
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()   
        return response.data

    def insertarContacto(self, nombre, email, telefono):
        datos = {"nombre": nombre, "email": email, "telefono": telefono}
        response = self.supabase.table("contactos").insert(datos).execute()
        return response.data

    def borrarContacto(self, id_contacto):
        response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
        return response.data

    def actualizarContacto(self, id_contacto, nombre, email, telefono):
        datos = {"nombre": nombre, "email": email, "telefono": telefono}
        response = self.supabase.table("contactos").update(datos).eq("id_contacto", id_contacto).execute()
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(1))
    #print(model_contactos.insertarContacto(1))
    print(model_contactos.borrarContacto("0"))
    #print(model_contactos.actualizarContacto(1))   

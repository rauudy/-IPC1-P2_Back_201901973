# Importamos la Clase Usuarios
from Usuarios import Usuarios

class MetodosUsu:
    # Constructor o inicializacion
    def __init__(self):
        self.usuarios=[]

    # Metodo para saber si existe ya un usuario determinado
    def existeuser(self,username):
        for x in self.usuarios:
            if x.username==username:
                return True
        return False

    # Metodo para recolectar a los usuarios
    def getusuarios(self):
        texto="[\n"
        for x in self.usuarios:
            texto+="{\"nombre\":\""+x.nombre+"\", \"apellido\": \""+x.apellido+"\", \"username\": \""+x.username+"\"}\n"
        texto+='\n]'
        return texto

    # Metodo para obtener la informacion de un usuario en especifico
    def getusuario(self,username):
        for x in self.usuarios:
            if x.username==username:
                return "{\"nombre\":\""+x.nombre+"\", \"apellido\": \""+x.apellido+"\", \"username\": \""+x.username+"\"}\n"
        return ""

    # Metodo para crear un usuario
    def crear(self,nombre,apellido,username,password):
        newuser = Usuarios(nombre,apellido,username,password)
        if self.existeuser(username):
            return False
        else:
            self.usuarios.append(newuser)
            return True

    # Metodo para iniciar sesion
    def iniciarsesion(self,username,password):
        for x in self.usuarios:
            if x.username==username and x.password==password:
                return True
        return False
    
    # Metodo para recuperar la contraseña
    def getpassword(self,username):
        for x in self.usuarios:
            if x.username==username:
                return "{\"data\":\""+x.password+"\"}"
        return ""
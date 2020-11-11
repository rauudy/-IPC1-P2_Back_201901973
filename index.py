from flask import Flask,request
from flask_cors import CORS
import json
from MetodosUsuarios import MetodosUsu

app = Flask(__name__)

CORS(app)

meth = MetodosUsu()

# Obtener los usuarios ya registrados
@app.route('/obtenerusuarios', methods=['GET'])
def usuarios():
    return meth.getusuarios()

# Crear un usuario
@app.route('/crear',methods=['POST'])
def crear():
    dato=request.json
    if meth.crear(dato['nombre'],dato['apellido'],dato['username'],dato['password']):
        return '{\"data\":\"Cuenta Creada con Exito\"}'
    else:
        return '{\"data\": \"Usuario ya existe, cambie nombre de Usuario\"}'

# Recuperar la contraseña de un usuario
@app.route('/recuperarContraseña',methods=['POST'])
def obtenerContraseña():
    dato=request.json
    if meth.existeuser(dato['username']):
        return meth.getpassword(dato['username'])

# Insertar muchos usuarios
@app.route('/masiva',methods=['POST'])
def insertarusuarios():
    dato=request.json
    for x in dato:
        meth.insertar(x['nombre'],x['apellido'],x['username'],x['password'])
    return 'Se ha insertado correctamente'

# prueba de insertar
@app.route('/masiva')
def insertarget():
    return 'ESTA ES MASIVA PERO CON GET'

# @app.route('/obteneruser/<username>')
#def obtenerid(username):
    #return meth.getusuario(username)


# iniciar sesion 
@app.route('/iniciarsesion',methods=['POST'])
def iniciarsesion():
    dato=request.json
    if dato['username'] =='admin' and dato['password'] == "admin":
        return "{\"data\":\"admin\"}"
    elif meth.iniciarsesion(dato['username'],dato['password']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"

@app.route('/cargaM', methods=['POST'])
def cargaM():
    data = request.json
    print(data)
    return data
    
# Ruta del Servidor Local
if __name__ == "__main__":
    app.run(port="5001",host="0.0.0.0",debug=True)  
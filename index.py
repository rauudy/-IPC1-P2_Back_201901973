from flask import Flask,request
from flask_cors import CORS
import json
from GestionUsuarios import Gestor

app = Flask(__name__)

CORS(app)

gestor = Gestor()


@app.route('/obtenerusuarios')
def usuarios():
    return gestor.getusuarios()

@app.route('/insertar',methods=['POST'])
def insertar():
    dato=request.json
    if gestor.insertar(dato['nombre'],dato['apellido'],dato['username'],dato['password']):
        return '{\"data\":\"Cuenta Creada con Exito\"}'
    else:
        return '{\"data\": \"Usuario ya existe\"}'

@app.route('/recuperarContraseña',methods=['POST'])
def obtenerContraseña():
    dato=request.json
    if gestor.existeuser(dato['username']):
        return gestor.getpassword(dato['username'])


@app.route('/masiva',methods=['POST'])
def insertar2():
    dato=request.json
    for x in dato:
        gestor.insertar(x['nombre'],x['apellido'],x['username'],x['password'])
    return 'Se ha insertado correctamente'




@app.route('/masiva')
def insertarget():
    return 'ESTA ES MASIVA PERO CON GET'

# @app.route('/obteneruser/<username>')
#def obtenerid(username):
    #return gestor.getusuario(username)



@app.route('/iniciarsesion',methods=['POST'])
def iniciarsesion():
    dato=request.json
    if dato['username'] =='admin' and dato['password'] == "admin":
        return "{\"data\":\"admin\"}"
    elif gestor.iniciarsesion(dato['username'],dato['password']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"
    

if __name__ == "__main__":
    app.run(port="5001",host="0.0.0.0",debug=True)  
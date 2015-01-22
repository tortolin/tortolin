'''
Created on 19/1/2015

@author: PC08
'''
from app import app
from ec.edu.itsae.dao import PersonaDAO
from flask import render_template, request, redirect, url_for

@app.route("/mainPersona")
def mainPersona():
    objR=PersonaDAO.PersonaDAo().reportarPersona()
    
    return render_template("prueba.html", data=objR)

@app.route("/addPersona", methods=['POST'])
def addPersona():
    nombre=request.form.get('nombre', type=str)
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)

    PersonaDAO.PersonaDAo().insertarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('mainPersona'))

@app.route("/buscarauto")
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objR=PersonaDAO.PersonaDAo().buscarPersonaNombre(nombre)
    print objR
    
    return objR

@app.route("/buscarDato")
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objR=PersonaDAO.PersonaDAo().buscarPersonaNombre(nombre)
    return render_template("prueba.html", data=objR)


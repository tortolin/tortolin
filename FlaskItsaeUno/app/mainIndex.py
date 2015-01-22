'''
Created on 19/1/2015

@author: PC08
'''
from ec.edu.itsae.dao import PersonaDAO
from app import app
from flask import render_template, request, redirect, url_for

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login")
def login():
    usuario=str(request.args.get('username'))
    clave=str(request.args.get('password'))
    report=PersonaDAO.PersonaDAo().validarusuario(usuario, clave)
    if len (report)==1:
        return redirect(url_for("main"))
    else:     
        return redirect (url_for("index"))

@app.route("/main")
def main():
    return render_template("main.html")

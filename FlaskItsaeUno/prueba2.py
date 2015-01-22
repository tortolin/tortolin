# coding:utf-8
'''
Created on 19/1/2015

@author: PC08
'''
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def inicio():
    X="Interaccion entre python & html"
    return render_template("prueba.html", dato=X)
if __name__ == '__main__':
    app.run("127.0.0.1", 5050, True)
    
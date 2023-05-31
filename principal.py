from flask import Flask, render_template, request, redirect
from py2neo import Graph, NodeMatcher
from prof import profile
app = Flask(__name__)


def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/princi.html', methods=['POST'])
def princi(usuario):

    #print("Usuario: ", usuari)

    return profile(usuario)

# @app.route('/perfil.html')
# def perfil():

#     global usuari

#     print("Usuario en el método perfil: ", usuari)

#     return profile(usuari)

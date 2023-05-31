from flask import Flask, render_template, request, redirect
from py2neo import Graph, NodeMatcher
from perfil import profile
app = Flask(__name__)


def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/principal.html', methods=['POST'])
def principal():

    #print("Usuario: ", usuari)

    return profile()

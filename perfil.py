from flask import Flask, render_template, request, redirect
from py2neo import Graph, Node, NodeMatcher

app = Flask(__name__)

def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/perfil.html', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        usu = request.form.get('delusuario')
        contra = request.form.get('delcontrasena')

        uri = "neo4j+s://ca536792.databases.neo4j.io"
        usuario = "neo4j"
        contrasena = "9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q"

        print("Usu: ", usu)
        print("Contra: ", contra)

        if usu and contra:
            try:
                graph = conectar(uri, usuario, contrasena)
                matcher = NodeMatcher(graph)
                nodo_usuario = matcher.match("Usuario", titulo=usu, contraseña=contra).first()

                print("Nodo usuario: ", nodo_usuario)

                if nodo_usuario:
                    graph.delete(nodo_usuario)
                    return render_template("index.html")
                else:
                    return render_template('perfil.html', resultado="Usuario y contraseña no encontrados.")
            except Exception as e:
                error_message = "Error al eliminar la cuenta: " + str(e)
                return render_template('perfil.html', resultado=error_message)
        else:
            return render_template('perfil.html', resultado="Usuario y contraseña requeridos.")

    return render_template('perfil.html', endpoint='index')
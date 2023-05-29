from flask import Flask, render_template, request, redirect
from py2neo import Graph, NodeMatcher

app = Flask(__name__)

def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/', methods=['GET', 'POST'])
def logins(uri, usuario, contrasena):
    if request.method == 'POST':
        usuario_input = request.form.get('usuario')
        contrasena_input = request.form.get('contrasena')

        # uri = "neo4j+s://ca536792.databases.neo4j.io"
        # usuario = "neo4j"
        # contrasena = "9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q"

        try:
            graph = conectar(uri, usuario, contrasena)
            matcher = NodeMatcher(graph)

            node = matcher.match("Cuenta", usuario=usuario_input, contrasena=contrasena_input).first()

            if node:
                # Credenciales válidas
                return success()
            else:
                # Credenciales inválidas
                return "No se ha encontrado la cuenta en la BDD"
        except Exception as e:
            print("Error al conectar a la base de datos:", str(e))
            return "Error al conectar a la base de datos"

    return render_template('login.html')

@app.route('/success2.html')
def success():
    #mensaje = "¡Registro exitoso! Gracias por registrarte."
    return render_template('success2.html')



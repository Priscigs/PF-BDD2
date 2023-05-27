from flask import Flask, render_template
from py2neo import Graph, Node

app = Flask(__name__)

def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/')
def index():
    try:
        graph = conectar(uri, usuario, contrasena)

        # Insertar un dato de prueba.
        node = Node("Person", name="Bob")
        graph.create(node)

        # Consultar el dato de prueba.
        result = graph.run("MATCH (a:Person) WHERE a.name = 'Bob' RETURN a.name AS name").data()

        print("Result: ", result)

        return render_template('index.html', result=result)

    except Exception as e:
        # Manejar la excepción si es necesario
        error_message = "Ocurrió un error: " + str(e)
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    uri = "neo4j+s://ca536792.databases.neo4j.io"
    usuario = "neo4j"
    contrasena = "9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q"
    app.run()

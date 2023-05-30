from flask import Flask, render_template, request, redirect
from py2neo import Graph, Node

app = Flask(__name__)

def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/', methods=['POST'])
def register(uri, usuario, contrasena):
    print("Request method:", request.method)

    if request.method == 'POST':
        usu = request.form.get('usuario')
        contra = request.form.get('contrasena')

        if usuario and contrasena:
            try:
                # Realiza las operaciones para guardar los datos en la base de datos
                graph = conectar(uri, usuario, contrasena)
                cuenta = Node("Cuenta", usuario=usu, contrasena=contra)
                graph.create(cuenta)

                return success()
            except Exception as e:
                error_message = "Error al registrar la cuenta: " + str(e)
                return render_template('register.html', resultado=error_message)
        else:
            return render_template('register.html', resultado="Usuario y contraseña requeridos.")

    return render_template('register.html')


@app.route('/success.html')
def success():
    #mensaje = "¡Registro exitoso! Gracias por registrarte."
    return render_template('success.html')

# Método para regresar al inicio.
@app.route('/index.html')
def index():
    return render_template('index.html')

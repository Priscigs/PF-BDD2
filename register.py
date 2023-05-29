from flask import Flask, render_template, request, redirect
from py2neo import Graph, Node

app = Flask(__name__)

def conectar(uri, usuario, contrasena):
    graph = Graph(uri, user=usuario, password=contrasena)
    return graph

@app.route('/', methods=['GET', 'POST'])
def register(uri, usuario, contrasena):
    if request.method == 'POST':
        user = request.form.get('usuario')
        passwords = request.form.get('contrasena')

        print("Usuario: ", usuario)
        print("Contraseña: ", passwords)

        if usuario and passwords:
            try:
                graph = conectar(uri, usuario, contrasena)
                cuenta = Node("Cuenta", usuario=user, contrasena=passwords)
                print("Cuenta: ", cuenta)

                graph.create(cuenta)

                return index()  # Redirigir a la página de éxito
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

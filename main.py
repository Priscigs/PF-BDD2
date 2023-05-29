from flask import Flask, render_template
from register import register
from login import logins

app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de registro
@app.route('/register.html', methods=['GET', 'POST'])
def register_route():

    uri = "neo4j+s://ca536792.databases.neo4j.io"
    usuario = "neo4j"
    contrasena = "9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q"

    return register(uri, usuario, contrasena)

# Ruta de inicio de sesión.
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    uri = "neo4j+s://ca536792.databases.neo4j.io"
    usuario = "neo4j"
    contrasena = "9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q"
    
    return logins(uri, usuario, contrasena)

if __name__ == '__main__':
    app.run()

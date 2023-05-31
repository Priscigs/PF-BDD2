from flask import Flask, render_template, request, redirect
from py2neo import Graph, NodeMatcher

app = Flask(__name__)
graph = Graph("neo4j+s://ca536792.databases.neo4j.io", auth=("neo4j", "9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q"))

# Método para actualizar la contraseña.
def actualizar_contrasena(user, nueva_contrasena):
    matcher = NodeMatcher(graph)
    nodo_usuario = matcher.match("Usuario", nombre=user).first()
    if nodo_usuario:
        nodo_usuario["contraseña"] = nueva_contrasena
        graph.push(nodo_usuario)
    
    return True

@app.route('/perfil.html', methods=['POST'])
def profile(user):
    
    print("Usuario: ", user)

    nueva_contra = request.form.get("newPassword")

    print("Nueva contraseña: ", nueva_contra)

    actualizar_contrasena(user, nueva_contra)

    return render_template("perfil.html")

@app.route('/borrado.html', methods=['POST'])
def borrar_perfil(user):
    # Realiza la lógica para borrar el perfil en la base de datos
    matcher = NodeMatcher(graph)
    nodo_usuario = matcher.match("Usuario", nombre=user).first()

    print("Nodo usuario: ", nodo_usuario)

    if nodo_usuario:
        graph.delete(nodo_usuario)
        return "Perfil borrado exitosamente"
    else:
        return "No se encontró el perfil en la base de datos"
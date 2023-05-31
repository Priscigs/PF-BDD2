from flask import Flask, render_template, request, redirect
from py2neo import Graph, NodeMatcher
from register import register
from login import logins
from import_data import *

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

@app.route('/genre.html')
def genre():
    return render_template('genre.html')

@app.route('/principal.html')
def principal():
    return render_template('principal.html')

@app.route('/profilePage.html')
def profilePage():
    return render_template('profilePage.html')

@app.route('/genre_action')
def genre_action():
    # Crear una conexión a la base de datos
    graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")

    # Consulta para obtener las películas relacionadas con el género "Action"
    query = """
    MATCH (:Genero {titulo: 'Action'})<-[:es_genero]-(p:Pelicula)
    RETURN p.titulo, p.duracion, p.año, p.rating
    """

    # Ejecutar la consulta y obtener los resultados
    result = graph.run(query)

    # Obtener los resultados como una lista de diccionarios
    movies = []
    for record in result:
        movie = {
            'titulo': record['p.titulo'],
            'duracion': record['p.duracion'],
            'ano': record['p.año'],
            'rating': record['p.rating']
        }
        movies.append(movie)

    # Renderizar la plantilla HTML y pasar los datos a la misma
    return render_template('genre_action.html', movies=movies)

@app.route('/genre_scifi')
def genre_scifi():
    # Crear una conexión a la base de datos
    graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")

    # Consulta para obtener las películas relacionadas con el género "Action"
    query = """
    MATCH (:Genero {titulo: 'Ciencia Ficcion'})<-[:es_genero]-(p:Pelicula)
    RETURN p.titulo, p.duracion, p.año, p.rating
    """

    # Ejecutar la consulta y obtener los resultados
    result = graph.run(query)

    # Obtener los resultados como una lista de diccionarios
    movies = []
    for record in result:
        movie = {
            'titulo': record['p.titulo'],
            'duracion': record['p.duracion'],
            'ano': record['p.año'],
            'rating': record['p.rating']
        }
        movies.append(movie)

    # Renderizar la plantilla HTML y pasar los datos a la misma
    return render_template('genre_scifi.html', movies=movies)

@app.route('/genre_com')
def genre_com():
    # Crear una conexión a la base de datos
    graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")

    # Consulta para obtener las películas relacionadas con el género "Action"
    query = """
    MATCH (:Genero {titulo: 'Comedy'})<-[:es_genero]-(p:Pelicula)
    RETURN p.titulo, p.duracion, p.año, p.rating
    """

    # Ejecutar la consulta y obtener los resultados
    result = graph.run(query)

    # Obtener los resultados como una lista de diccionarios
    movies = []
    for record in result:
        movie = {
            'titulo': record['p.titulo'],
            'duracion': record['p.duracion'],
            'ano': record['p.año'],
            'rating': record['p.rating']
        }
        movies.append(movie)

    # Renderizar la plantilla HTML y pasar los datos a la misma
    return render_template('genre_com.html', movies=movies)

@app.route('/genre_drama')
def genre_drama():
    # Crear una conexión a la base de datos
    graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")

    # Consulta para obtener las películas relacionadas con el género "Action"
    query = """
    MATCH (:Genero {titulo: 'Drama'})<-[:es_genero]-(p:Pelicula)
    RETURN p.titulo, p.duracion, p.año, p.rating
    """

    # Ejecutar la consulta y obtener los resultados
    result = graph.run(query)

    # Obtener los resultados como una lista de diccionarios
    movies = []
    for record in result:
        movie = {
            'titulo': record['p.titulo'],
            'duracion': record['p.duracion'],
            'ano': record['p.año'],
            'rating': record['p.rating']
        }
        movies.append(movie)

    # Renderizar la plantilla HTML y pasar los datos a la misma
    return render_template('genre_drama.html', movies=movies)

@app.route('/genre_horror')
def genre_horror():
    # Crear una conexión a la base de datos
    graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")

    # Consulta para obtener las películas relacionadas con el género "Action"
    query = """
    MATCH (:Genero {titulo: 'Horror'})<-[:es_genero]-(p:Pelicula)
    RETURN p.titulo, p.duracion, p.año, p.rating
    """

    # Ejecutar la consulta y obtener los resultados
    result = graph.run(query)

    # Obtener los resultados como una lista de diccionarios
    movies = []
    for record in result:
        movie = {
            'titulo': record['p.titulo'],
            'duracion': record['p.duracion'],
            'ano': record['p.año'],
            'rating': record['p.rating']
        }
        movies.append(movie)

    # Renderizar la plantilla HTML y pasar los datos a la misma
    return render_template('genre_horror.html', movies=movies)

@app.route('/genre_rom')
def genre_rom():
    # Crear una conexión a la base de datos
    graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")

    # Consulta para obtener las películas relacionadas con el género "Action"
    query = """
    MATCH (:Genero {titulo: 'Romance'})<-[:es_genero]-(p:Pelicula)
    RETURN p.titulo, p.duracion, p.año, p.rating
    """

    # Ejecutar la consulta y obtener los resultados
    result = graph.run(query)

    # Obtener los resultados como una lista de diccionarios
    movies = []
    for record in result:
        movie = {
            'titulo': record['p.titulo'],
            'duracion': record['p.duracion'],
            'ano': record['p.año'],
            'rating': record['p.rating']
        }
        movies.append(movie)

    # Renderizar la plantilla HTML y pasar los datos a la misma
    return render_template('genre_rom.html', movies=movies)

@app.route('/delete')
def delete():
    return render_template('/delete.html')

@app.route('/modifyP')
def modifyP():
    return render_template('/modifyP.html')

@app.route('/deleteR')
def deleteR():
    return render_template('/deleteR.html')

@app.route('/deletePR')
def deletePR():
    return render_template('/deletePR.html')

@app.route('/eliminar-cuenta', methods=['POST'])
def eliminar_cuenta():
    if request.method == 'POST':
        usuario_input = request.form.get('delusuario')
        contrasena_input = request.form.get('delcontrasena')

        try:
            # Crear una conexión a la base de datos
            graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")
            matcher = NodeMatcher(graph)

            node = matcher.match("Usuario", titulo=usuario_input, contraseña=contrasena_input).first()

            if node:
                # Eliminar el nodo de la cuenta
                graph.delete(node)
                return "Cuenta eliminada exitosamente."
            else:
                return "No se ha encontrado la cuenta en la base de datos."
        except Exception as e:
            print("Error al conectar a la base de datos:", str(e))
            return "Error al conectar a la base de datos."

    return redirect('/')

@app.route('/modificar-contrasena', methods=['POST'])
def modificar_contrasena():
    if request.method == 'POST':
        usuario_input = request.form.get('delusuario')
        contrasena_input = request.form.get('delcontrasena')
        nueva_contrasena_input = request.form.get('delcontrasena1')

        try:
            # Crear una conexión a la base de datos
            graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")
            matcher = NodeMatcher(graph)

            node = matcher.match("Usuario", titulo=usuario_input, contraseña=contrasena_input).first()

            if node:
                # Modificar la contraseña del nodo de usuario
                node['contraseña'] = nueva_contrasena_input
                graph.push(node)
                return "Contraseña modificada exitosamente."
            else:
                return "No se ha encontrado la cuenta en la base de datos."
        except Exception as e:
            print("Error al conectar a la base de datos:", str(e))
            return "Error al conectar a la base de datos."

    return redirect('/')

@app.route('/eliminar-rating', methods=['POST'])
def eliminar_rating():
    if request.method == 'POST':
        titulo_input = request.form.get('titulo')

        try:
            # Crear una conexión a la base de datos
            graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")
            matcher = NodeMatcher(graph)

            node = matcher.match("Pelicula", titulo=titulo_input).first()

            if node:
                # Eliminar la propiedad 'rating' del nodo de película
                node.pop('rating')
                graph.push(node)
                return "La propiedad 'rating' ha sido eliminada del nodo de película."
            else:
                return "No se ha encontrado la película en la base de datos."
        except Exception as e:
            print("Error al conectar a la base de datos:", str(e))
            return "Error al conectar a la base de datos."

    return redirect('/')

@app.route('/eliminar-PR', methods=['POST'])
def eliminar_PR():
    if request.method == 'POST':
        titulo_input = request.form.get('titulo')

        try:
            # Crear una conexión a la base de datos
            graph = Graph(uri="neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")
            matcher = NodeMatcher(graph)

            node = matcher.match("Pelicula", titulo=titulo_input).first()

            if node:
                # Eliminar la propiedad 'rating' del nodo de película
                for rel in node.relationships:

                    if rel.type == 'es_genero':
                        rel.pop('es_genero')
                        graph.push(rel)

                return "La propiedad 'es_genero' de la releación de la película fue eliminada."
            else:
                return "No se ha encontrado la película en la base de datos."
        except Exception as e:
            print("Error al conectar a la base de datos:", str(e))
            return "Error al conectar a la base de datos."

    return redirect('/')

if __name__ == '__main__':
    app.run()

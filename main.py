from flask import Flask, render_template
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

@app.route('/genre_movies')
def genre_movies():
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
    return render_template('genre_movies.html', movies=movies)


if __name__ == '__main__':
    app.run()

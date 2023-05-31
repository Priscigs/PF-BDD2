from py2neo import Graph, Node
from datetime import datetime
import pandas as pd
graph = Graph(uri= "neo4j+s://ca536792.databases.neo4j.io", user="neo4j", password="9kEkEZcx8aTRfBKerXNxeEw8U1P9FNSH1Zvu1a4dG2Q")
#Creando generos.
# generos = ["Action","Ciencia Ficcion", "Comedy", "Drama","Horror","Romance"]

# for genero in generos:
#     generoN = Node("Genero", titulo = genero)
#     graph.create(generoN)

#leer los archivos csv con pandas
catalogo = pd.read_csv("Peliculas.csv")
simis = pd.read_csv("Similitudes.csv")
rates = pd.read_csv("Ratings.csv")
# titulos = []
# titulos.extend(catalogo['Titulo'])
# duras = []
# duras.extend(catalogo['Duración'])
# anos = []
# anos.extend(catalogo['Año'])
# ratings = []
# ratings.extend(catalogo['Rating'])
# generos = []
# generos.extend(catalogo['Genero'].tolist())

# for row in range(len(titulos)):
#     titulo = titulos[row]
#     dura = int(duras[row])
#     ano = str(anos[row])
#     anio= datetime.strptime(ano, "%Y").date()
#     rating = int(ratings[row])
#     gene = [generos[row]]
#     gener=generos[row]
#     query1="CREATE (p:Pelicula {titulo:'"+titulo+"', duracion:toFloat('"+str(dura)+"'),  año:date('" + str(anio) + "'), rating:toFloat('"+str(rating)+"'),genero:$gene})"
#     result = graph.run(query1,gene=gene)
#     query2= "MATCH (a:Pelicula{titulo:'"+titulo+"'}),(b:Genero{titulo:'"+gener+"'}) MERGE (a)-[r:es_genero]->(b)"
#     result2 = graph.run(query2)

#obteniendo elementos de ratings y metiendolos a listas
# usuarios = []
# usuarios.extend(rates['Usuario'].tolist())
# peliculas = []
# peliculas.extend(rates['Pelicula'].tolist())
# ratings2 = []
# ratings2.extend(rates['Rating'].tolist())
# password = []
# password.extend(rates['password'].tolist())
# for row in range(len(usuarios)):
#     usuario = usuarios[row]
#     pelicula = peliculas[row]
#     rating2 = str(ratings2[row])
#     passwor= password[row]
#     query1="CREATE (p:Usuario {titulo:'"+usuario+"', contraseña:'"+passwor+"'})"
#     result = graph.run(query1)
#     query2= "MATCH (a:Usuario {titulo:'"+usuario+"'}), (b:Pelicula {titulo:'"+pelicula+"'}) MERGE (a)-[r:has_rated{rating:toFloat('"+rating2+"')}]->(b)"
#     result2 = graph.run(query2)

#obteniendo elementos de similitudes y metiendolas a listas
pelis1 = []
pelis1.extend(simis['Pelicula1'].tolist())
pelis2 = []
pelis2.extend(simis['Pelicula2'].tolist())

#for loop para poder crear las relaciones entre peliculas similares de diferentes generos
for row in range(len(pelis1)):
    pelicula1 = pelis1[row]
    pelicula2 = pelis2[row]
    query1= "MATCH (a:Pelicula{titulo:'"+pelicula1+"'}),(b:Pelicula{titulo:'"+pelicula2+"'}) MERGE (a)-[r:similar]->(b)"
    result2 = graph.run(query1)

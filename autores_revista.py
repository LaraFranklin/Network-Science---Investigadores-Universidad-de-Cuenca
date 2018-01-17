import csv
import networkx as nx
from itertools import combinations

grafo = nx.Graph()
diccionario = {}
with open('AutoresSource.csv') as csv_file:
    for autores,revista  in csv.reader(csv_file, delimiter=';'):
        listaAutores = []
        for autor in autores.split(","):
            listaAutores.append(autor)
        if diccionario.__contains__(revista):
            lista = diccionario[revista]
            for i in lista:
                listaAutores.append(i)
        diccionario[revista] = listaAutores
        datos = list(diccionario.values())

for revista, autores in diccionario.items():
    for  autor in autores:
        if grafo.has_edge(revista, autor):
            grafo[revista][autor]['weight'] = grafo[revista][autor]['weight'] + 1
        else:
            grafo.add_weighted_edges_from([(revista, autor, 1)])
nx.write_gml(grafo,'AutoresSource.gml')

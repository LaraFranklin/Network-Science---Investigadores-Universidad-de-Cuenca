import csv
import networkx as nx
from itertools import combinations

grafo = nx.Graph()
with open('autores.csv') as csv_file:
    for row in csv.reader(csv_file, delimiter=','):
        lista_docs = []
        for dos in row:
            lista_docs.append(dos)
        docentes = combinations(lista_docs, 2)
        for docente in docentes:
            if grafo.has_edge(docente[0], docente[1]):
                grafo[docente[0]][docente[1]]['weight'] = grafo[docente[0]][docente[1]]['weight'] + 1
            else:
                grafo.add_weighted_edges_from([(docente[0], docente[1], 1)])
nx.write_gml(grafo, 'red_autores.gml')
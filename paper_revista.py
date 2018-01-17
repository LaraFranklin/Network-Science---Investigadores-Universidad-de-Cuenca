import csv
import networkx as nx
from itertools import combinations

dict_fn = {}
grafo = nx.Graph()
with open('data_co_autores.csv') as csv_file:
    for row in csv.reader(csv_file, delimiter=','):
        revista = row[len(row) - 1]
        del row[len(row) - 1]

        for autor in row:
            if autor in dict_fn:
                revistas = set([revista]).union(dict_fn[autor])
            else:
                revistas = set([revista])
            dict_fn[autor] = revistas

for revista in dict_fn:
    comb = combinations(dict_fn[revista], 2)
    for comb_tem in comb:
        if grafo.has_edge(comb_tem[0], comb_tem[1]):
            grafo[comb_tem[0]][comb_tem[1]]['weight'] = grafo[comb_tem[0]][comb_tem[1]]['weight'] + 1
        else:
            grafo.add_weighted_edges_from([(comb_tem[0], comb_tem[1], 1)])

nx.write_gml(grafo, 'data_revista_paper.gml')






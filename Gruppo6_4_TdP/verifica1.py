from Gruppo6_4_TdP.pkg_1.my_graph import MyGraph
from util import randList
import time
# primo test
grafo1 = MyGraph()

v0 = grafo1.insert_vertex(0)
v1 = grafo1.insert_vertex(1)
v2 = grafo1.insert_vertex(2)
v3 = grafo1.insert_vertex(3)
v4 = grafo1.insert_vertex(4)
v5 = grafo1.insert_vertex(5)
v6 = grafo1.insert_vertex(6)
v7 = grafo1.insert_vertex(7)
v8 = grafo1.insert_vertex(8)
v9 = grafo1.insert_vertex(9)
v10 = grafo1.insert_vertex(10)

grafo1.insert_edge(v0, v1)
grafo1.insert_edge(v1, v2)
grafo1.insert_edge(v2, v3)
grafo1.insert_edge(v3, v4)
grafo1.insert_edge(v2, v5)
grafo1.insert_edge(v5, v6)
grafo1.insert_edge(v2, v7)
grafo1.insert_edge(v8, v7)

grafo1.insert_edge(v4, v9)
grafo1.insert_edge(v9, v10)
grafo1.insert_edge(v9, v6)

grafo1.insert_edge(v3, v7)
grafo1.insert_edge(v1, v7)
grafo1.insert_edge(v1, v5)
grafo1.insert_edge(v3, v5)
print("Primo test:")
print("GREEDY")
vertici = grafo1.greedy_vertex_cover()
for vertice in vertici:
    print(vertice)
print("MIN")
vertici = grafo1.min_vertex_cover()

for vertice in vertici:
    print(vertice)

# secondo test

grafo2 = MyGraph()

v0 = grafo2.insert_vertex(0)
v1 = grafo2.insert_vertex(1)
v2 = grafo2.insert_vertex(2)

grafo2.insert_edge(v0, v1)
grafo2.insert_edge(v1, v2)
grafo2.insert_edge(v2, v0)

vertici = grafo2.min_vertex_cover()
print("Secondo test:")
print("GREEDY")
vertici = grafo2.greedy_vertex_cover()
for vertice in vertici:
    print(vertice)
print("MIN")
vertici = grafo2.min_vertex_cover()

for vertice in vertici:
    print(vertice)

# terzo test

grafo3 = MyGraph()

v0 = grafo3.insert_vertex(0)
v1 = grafo3.insert_vertex(1)
v2 = grafo3.insert_vertex(2)
v3 = grafo3.insert_vertex(3)
v4 = grafo3.insert_vertex(4)
v5 = grafo3.insert_vertex(5)
v6 = grafo3.insert_vertex(6)

grafo3.insert_edge(v0, v1)
grafo3.insert_edge(v0, v2)
grafo3.insert_edge(v1, v2)
grafo3.insert_edge(v1, v6)
grafo3.insert_edge(v1, v3)
grafo3.insert_edge(v3, v5)
grafo3.insert_edge(v1, v4)
grafo3.insert_edge(v4, v5)

print("Terzo test:")
print("GREEDY")
vertici = grafo3.greedy_vertex_cover()
for vertice in vertici:
    print(vertice)
print("MIN")
vertici = grafo3.min_vertex_cover()

for vertice in vertici:
    print(vertice)

#inizializzazione grafi
n_grafi = randList(51, 60, 1)[0]
grafi = []

for i in range(n_grafi):
    grafo = MyGraph()
    n_vertici = randList(51, 60, 1)[0]
    lista_vertici = []

    for vertice in range(0, n_vertici):
        lista_vertici.append(grafo.insert_vertex(vertice))
    for vertice in grafo.vertices():
        n_archi = randList(1, 5, 1)[0]
        archi_random = randList(0, n_vertici-1, n_archi)
        vertici_adiacenti = []
        while len(archi_random) != 0:
            vertici_adiacenti.append(lista_vertici[archi_random.pop()])
        for adiacente in vertici_adiacenti:
            try:
                grafo.insert_edge(vertice, adiacente)
            except ValueError:
                continue

    grafi.append(grafo)
    greedy_time = time.time()
    greedy = grafi[i].greedy_vertex_cover()
    greedy_end_time = time.time() - greedy_time
    print("Lunghezza greedy vertex cover:")
    print(len(greedy), grafo.vertex_count())
    print("Tempo di esecuzione greedy:", greedy_end_time)
    print("Lunghezza min vertex cover: ")
    mvc_time = time.time()
    mvcs = grafi[i].min_vertex_cover()
    mvc_end_time = time.time() - mvc_time
    print(len(mvcs))
    print("Tempo di esecuzione min_vertex_cover:", mvc_end_time)

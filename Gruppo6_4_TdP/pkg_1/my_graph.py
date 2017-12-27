import copy
from TdP_collections.graphs.graph import Graph


class MyGraph(Graph):

    class Vertex(Graph.Vertex):
        __slots__ = '_cd'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            super().__init__(x)
            self._cd = 0

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        super().insert_edge(u, v, x)
        u._cd += 1
        v._cd += 1

    def min_vertex_cover(self):
        lsf, min_vcs = self._last_vertex_cover()
        min_vcs.sort(key=len)
        return min_vcs[0]

    def _last_vertex_cover(self, **params):
        """ Inizializzazione
            k = numero di vertici da coprire
            uncov = numero di archi da coprire
            opt = minimo numero di archi scoperti trovati finora
            free_vertices = vertici marcati come free, ancora da esplorare,
            o liberi a causa del backtracking
            covered_vertices
            covered_vertices = vertici marcati come coperti
            uncovered_vertices = vertici marcati come scoperti
            lsf = rappresenta l'ultima soluzione trovata
            min_vcs = rappresenta l'insieme di copertura minimo trovato finora.
            """
        if not params:
            k = self.vertex_count()
            uncov = self.edge_count()
            opt = uncov
            free_vertices = []
            for vertex in self.vertices():
                free_vertices.append(vertex)
            covered_vertices = []
            uncovered_vertices = []
            lsf = []
            min_vcs = []
        elif len(params) != 8:
            raise ValueError("Il metodo è stato chiamato con un numero di parametri non previsto.")
        else:
            # Inizializzazione dei parametri passati alle successive chiamate ricorsive.
            k = params["k"]
            uncov = params["uncov"]
            opt = params["opt"]
            free_vertices = params["free_vertices"]
            covered_vertices = params["covered_vertices"]
            uncovered_vertices = params["uncovered_vertices"]
            lsf = params["lsf"]
            min_vcs = params["min_vcs"]

        if k == 0:
            lsf = copy.deepcopy(covered_vertices)
            return lsf, min_vcs
        if uncov < opt:
            opt = uncov
            lsf.clear()
            lsf = copy.deepcopy(covered_vertices)
            if uncov == 0:
                min_vcs.append(copy.deepcopy(covered_vertices))
        if self._bounding(uncov, opt):
            return lsf, min_vcs

        def cover_degree(vertex):
            return vertex._cd

        free_vertices.sort(key=cover_degree)
        try:
            i = free_vertices.pop()
        except IndexError:
            return lsf, min_vcs
        covered_vertices.append(i)
        k -= 1
        self._fix_neighbours_degree(i)
        lsf = self._last_vertex_cover(k=k, uncov=uncov-i._cd, opt=opt,
                                    free_vertices=free_vertices, covered_vertices=covered_vertices,
                                    uncovered_vertices=uncovered_vertices, lsf=lsf, min_vcs=min_vcs)[0]
        covered_vertices.pop()
        uncovered_vertices.append(i)
        k += 1
        self._fix_neighbours_degree(i, False)

        lsf = self._last_vertex_cover(k=k, uncov=uncov, opt=opt,
                                    free_vertices=free_vertices, covered_vertices=covered_vertices,
                                    uncovered_vertices=uncovered_vertices, lsf=lsf, min_vcs=min_vcs)[0]
        uncovered_vertices.pop()
        free_vertices.append(i)
        return lsf, min_vcs

    def _fix_neighbours_degree(self, i, covered=True):
        if covered:
            for edge in self.incident_edges(i):
                edge.opposite(i)._cd -= 1
        else:
            for edge in self.incident_edges(i):
                edge.opposite(i)._cd += 1

    def _bounding(self, uncover, opt):
        lb = max(0, uncover)
        if lb > opt or uncover == 0:
            return True
        else:
            return False

    def delete_edge(self, u, v):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        del self._outgoing[u][v]
        del self._incoming[v][u]

    def greedy_vertex_cover(self):

        my_graph = copy.deepcopy(self)

        solution = []
        vertices = []

        for vertex in my_graph.vertices():
            vertices.append(vertex)
        vertices.sort(key=my_graph._sort_desc_degree)

        while my_graph.edge_count() != 0:
            max_vertex = vertices.pop()
            solution.append(max_vertex)

            while my_graph.degree(max_vertex) != 0:
                incident = my_graph.incident_edges(max_vertex).__next__() #trovare un modo più elegante
                opposite = incident.opposite(max_vertex)

                try:
                    vertices.remove(opposite)
                except:
                    continue
                finally:
                    my_graph.delete_edge(max_vertex, opposite)


        return solution




    def _sort_desc_degree(self, vertex):

        return self.degree(vertex)


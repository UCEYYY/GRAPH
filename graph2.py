class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_vertex(self):
        return list(self.gdict.keys())

    def get_edges(self):
        edges = []
        for v in self.gdict:
            for e in self.gdict[v]:
                if {v, e} not in edges:
                    edges.append({v, e})
        return edges

    def add_vertex(self, v):
        if v not in self.gdict:
            self.gdict[v] = []

    def add_edge(self, e):
        (v1, v2) = e
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = [v2]
        if v2 in self.gdict:
            self.gdict[v2].append(v1)
        else:
            self.gdict[v2] = [v1]

# Membuat dictionary dengan elemen graph
graph1 = {1: [2, 3],
         2: [1, 2], 
         3: [1, 4], 
         4: [5], 
         5: [4]}
#print graph
g = Graph(graph1)
print("Awal       : ", g.get_vertex())
print("Awal       : ", g.get_edges())
print("Awal       : ", g.get_vertex())
print("Awal       : ", g.get_edges())
g.add_vertex(6)
print("Tambah     : ", g.get_vertex())
g.add_edge({1, 2})
print("Tambah     : ", g.get_edges())
g.add_edge({6, 1})
print("Tambah ke-2: ", g.get_vertex())
print("Tambah ke-2: ", g.get_edges())
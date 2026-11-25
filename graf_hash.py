class GrafHash:

    def __init__(self, ln=None, lv=None, lp=None):
        if lp==None:
            lp=[None]*len(lv)
        self._num=0
        self._nodes={}
        if ln:
            for n in ln:
                self.insert_vertex(n)
        if lv:
            for i,p in zip(lv,lp):
                self.insert_edge(i[0],i[1],p)

    def insert_vertex(self, x) -> None:
        self._nodes[x]={}

    def insert_edge(self, n1, n2, p=1) -> None:
        self.aresta(n1,n2,p)
        self.aresta(n2,n1,p)
        self._num+=1

    def aresta(self, n1, n2, p) -> None:
       self._nodes[n1][n2]=p
       

    def antiaresta(self, n1, n2) -> None:
           del self._nodes[n1][n2]

    def remove_edge(self, n1, n2) -> None:
        self.antiaresta(n1,n2)
        self.antiaresta(n2,n1)
        self._num-=1

    def remove_vertex(self, x) -> None:
        veins=list(self._nodes[x].keys())
        if veins:
            for vei in veins:
                self.remove_edge(vei,x)
        del self._nodes[x]

    def has_edge(self, n1, n2) -> bool:
        try:
            p=self._nodes[n1][n2]
        except:
            return False
        return True

    def weight(self, n1, n2):
        if n2 in self._nodes[n1]:
            return self._nodes[n1][n2]
        else:
            return None

    def degree(self, x) -> int:
        return len(self._nodes[x])

    def num_vertices(self) -> int:
        return len(self._nodes)

    def num_edges(self) -> int:
        return self._num

    def vertices(self):
        return list(self._nodes.keys())

    def edges(self, x):
        return list(self._nodes[x].keys())


g = GrafHash(["Sants Est.", "Pl. Sants", "Hostafr."],
             [["Sants Est.", "Pl. Sants"], ["Pl. Sants", "Hostafr."]],
             [1585, 511])

print(g.num_edges())
g.insert_vertex("Esp.")
g.insert_edge("Hostafr.", "Esp.")       # sense pes: pes 1

print(g.num_edges())                           # retorna 3


g.remove_vertex("Pl. Sants")

print(g.num_edges())                           # retorna 1

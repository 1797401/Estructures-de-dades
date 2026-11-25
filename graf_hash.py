class GrafHash:

    def __init__(self, ln=None, lv=None, lp=None):
        lp=[None]*len(lv)
        self._num=0
        self._nodes={}
        if lv:
            for i,p in zip(lv,lp):
                self.insert_edge(i[0],i[1],p)

    def insert_vertex(self, x) -> None:
        self._nodes[x]={}

    def insert_edge(self, n1, n2, p=1) -> None:
        self.aresta(n1,n2,p)
        self.aresta(n2,n2,p)
        self._num+=1

    def aresta(self, n1, n2, p) -> None:
       self._nodes[n1][n2]=p
       

    def antiaresta(self, n1, n2, p) -> None:
           del self._nodes[n1][n2]

    def remove_edge(self, n1, n2) -> None:
        self.aresta(n1,n2)
        self.aresta(n2,n2)
        self._num-=1

    def remove_vertex(self, x) -> None:
        veins=self._nodes[x].keys()
        for vei in veins:
            del self._nodes[vei][x]
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
        return self._nodes.keys()

    def edges(self, x):
        return self._nodes[x].keys()

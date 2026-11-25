class GrafHash:

    def __init__(self, ln=None, lv=None, lp=None):
        self._num=0
        self._nodes={}
        if ln is not None:
            for n in ln:
                self.insert_vertex(n)
        if lv is not None and lp is not None:
            for i,p in zip(lv,lp):
                self.insert_edge(i[0],i[1],p)
        elif lv is not None:
            for i in lv:
                self.insert_edge(i[0],i[1])

    def insert_vertex(self, x) -> None:
        if x not in self._nodes:
            self._nodes[x]={}

    def insert_edge(self, n1, n2, p=1) -> None:
        if n1 not in self._nodes[n2] and n2 not in self._nodes[n1]:
            self.aresta(n1,n2,p)
            self.aresta(n2,n1,p)
            self._num+=1
        else:
            self._nodes[n1][n2]=p
            self._nodes[n2][n1]=p

    def aresta(self, n1, n2, p) -> None:
       self._nodes[n1][n2]=p
       

    def antiaresta(self, n1, n2) -> None:
           del self._nodes[n1][n2]

    def remove_edge(self, n1, n2) -> None:
        if self.has_edge(n1,n2):
            self.antiaresta(n1,n2)
            self.antiaresta(n2,n1)
            self._num-=1

    def remove_vertex(self, x) -> None:
        if x in self._nodes:
            veins=list(self._nodes[x].keys())
            self._num-=len(veins)
            if veins:
                for vei in veins:
                    del self._nodes[vei][x]
            del self._nodes[x]

    def has_edge(self, n1, n2) -> bool:
        return n1 in self._nodes and n2 in self._nodes[n1]

    def weight(self, n1, n2):
        if n1 in self._nodes and n2 in self._nodes[n1]:
            return self._nodes[n1][n2]
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



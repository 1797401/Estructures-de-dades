# Estats d'una posició de la taula (hash tancat). NO canvieu aquests valors.
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [[None, None, LLIURE]]   # m posicions, inicialment buides
        self._n = 0                                    # nombre de claus desades
        self._m = cap               

    def _hash_function(self, key):
        return key % self._m          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        self._table[self._trobar_forat(key, key)] = [key, value, OCUPAT]
        if self._n>self._m/2:
                    self.redimendionament()


    def get(self, key: int) -> int:
        r = self._cerca(key, key, self._m)
        if r == -1:
            return r
        else:
            return self._table[r][1]

    def remove(self, key: int) -> None:
        r= self._cerca(key, key, self._m)
        if r != -1:
            self._table[r]=[None, None, ESBORRAT]
            self._n -= 1

    def __len__(self):
        return self._n


    def _cerca(self, i, key, c):
        j = self._hash_function(i)
        if c == 0:
            return -1
        elif self._table[j][2] == LLIURE:
            return -1
        elif self._table[j][2] == ESBORRAT:
            return self._cerca(i+1, key, c-1)
        else:
            if key == self._table[j][0]:
                return j
            else:
                return self._cerca(i+1, key, c+1)
        
        

    def _trobar_forat(self, i, key):
        j = self._hash_function(i)
        if self._table[j][2] == LLIURE:
            self._n += 1
            return j
        elif self._table[j][2] == ESBORRAT:
            for x,y in enumerate(self._table):
                if y[0] == key:
                    return x
            self._n += 1
            return j
        else:
            if self._table[j][0] == key:
                return j
            else:
                return self._trobar_forat(i+1, key)

    def __str__(self):
        t=""
        for x,i in enumerate(self._table):
            if i[2] != LLIURE:
                t+=(f"posicio: {x} info:{i[0]},{i[1]}, ")

        return t

    def redimendionament(self):
            print("intent")
            self._m = self._m*2-1
            vell_hash = self._table
            self._table = self._m*[None]
            self._n=0
            for i in vell_hash:
                if i != None:
                    for sub in i:
                        self.put(sub[0], sub[1])
            print("aconseguio")

    



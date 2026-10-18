class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades
        self._m = cap                  

    def _hash_function(self, key):
        return key % self._m          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        if self._table[j] is None:             # posició lliure
            self._table[j] = [[key, value]]
            self.augment_n()
            return None

        else:
            for i in self._table[j]:
                if i[0] == key:
                    i[1] = value
                    return None

            self._table[j].append([key,value])
            self.augment_n()
            return None
                



    def get(self, key: int) -> int:
        j = self._hash_function(key)
        if self._table[j] is not None:
            for i in self._table[j]:
                if i[0] == key:
                    return i[1]
        return -1

    def remove(self, key: int) -> None:
        j  = self._hash_function(key)
        if self._table[j] is not None:
            for i in self._table[j]:
                if i[0] == key:
                    self._table[j].remove(i)
                    self._n-=1
                    return None
        return -1

    
    def __len__(self):
        return self._n

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


    def augment_n(self):
        self._n+=1
        if self._n>self._m/2:
            self.redimendionament()



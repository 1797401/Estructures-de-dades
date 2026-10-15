class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        if self._table[j] is None:             # posició lliure
            self._table[j] = [[key, value]]
            self._n += 1
            return None

        else:
            for i in self._table[j]:
                if i[0] == key:
                    i[1] = value
                    self._n += 1
                    return None

            self._table[j].append([key,value])
            self._n += 1
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
                    self._n=-1
        return -1

    
    def __len__(self):
        return self._n
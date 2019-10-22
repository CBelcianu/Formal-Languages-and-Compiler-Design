from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.ht = HashTable()

    def add(self, key, value):
        return self.ht.add(key, value)

    def get(self, value):
        return self.ht.getKey(value)

    def __str__(self):
        return str(self.ht)

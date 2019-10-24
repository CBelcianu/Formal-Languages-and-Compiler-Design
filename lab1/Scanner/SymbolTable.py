from HashTable import HashTable
from SortedTable import SortedTable


class SymbolTable:
    def __init__(self):
        self.st = SortedTable()

    def add(self,  value):
        return self.st.add(value)

    def get(self, value):
        return self.st.getID(value)

    def __str__(self):
        return str(self.st)

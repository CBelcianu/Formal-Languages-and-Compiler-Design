class HashTable(object):
    def __init__(self, length=10):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def resolveCollision(self, value):
        for i in range(len(self.array)):
            if self.array[i] is None:
                self.array[i] = [[i, value]]
                return

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key and not self.get(index) == value:
                    self.resolveCollision(value)
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])
        for i in range(len(self.array)):
            if self.array[i] is not None:
                self.array[i] = [self.array[i][0]]
        return index

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            raise KeyError()

    def getKey(self, value):
        for i in self.array:
            if value in i:
                return i
        return -1

    def isFull(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1
        return items > len(self.array) / 2

    def double(self):
        ht2 = HashTable(length=len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for kvp in self.array[i]:
                ht2.add(kvp[0], kvp[1])

        self.array = ht2.array

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __str__(self):
        res = "\n"
        for i in self.array:
            if i is not None:
                res += str(i) + '\n'
        return res

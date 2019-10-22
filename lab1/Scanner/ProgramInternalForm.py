class ProgramInternalForm:
    def __init__(self):
        self.array = []

    def add(self, code, uid):
        self.array.append([code, uid])

    def __str__(self):
        res = "\n"
        for i in self.array:
            if i is not None:
                res += str(i) + '\n'
        return res

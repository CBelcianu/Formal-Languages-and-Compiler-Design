class SortedTable(object):
    def __init__(self):
        self.table=[]
        self.count=0

    def add(self,value):
        id=self.getID(value)
        if id!=-1:
            return id
        self.table.append((value,self.count))
        self.count+=1
        self.table=sorted(self.table, key=lambda x:x[0])
        return self.count-1

    def getID(self, value):
        for i in self.table:
            if i[0]==value:
                return i[1]
        return -1

    def __str__(self):
        return str(self.table)
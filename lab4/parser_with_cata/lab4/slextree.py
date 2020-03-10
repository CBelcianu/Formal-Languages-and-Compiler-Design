def power_of_2_factor_lt(value) :
    """ computes the largest power of two smaller than the given value """
    pw = 1
    while pw < value :
        pw *= 2
    if pw == 1:
        return 0
    elif value == pw:
        return pw
    else :
        return pw//2

class Slextree :
    def __init__(self) :
        self.v = [None, None]

    def search(self, data):
        i = 1
        while i < len(self.v) and self.v[i] != None :
            if self.v[i].value > data.value :
                i = 2*i
            elif self.v[i].value < data.value :
                i = 2*i+1
            else: # it founds the value
                return i
        if i < len(self.v) : # it founds the position and it is None
            return i
        else : # it founds the position but it is not yet defined
            return -i 
    
    def append(self, data) :
        i = self.search(data)
        if i < 1 :
            i *= -1
            for j in range(power_of_2_factor_lt(i)) :
                self.v.append(None)
        self.v[i] = data
        
## testing
# tree = Slextree()
# tree.append("i")
# tree.append("c")
# tree.append("k")
# tree.append("j")
# tree.append("m")
# tree.append("a")
# tree.append("d")
# print(tree.v)
        

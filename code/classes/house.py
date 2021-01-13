import battery

class House(object):

    def __init__(self,id, x, y, maxoutput):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.maxoutput = float(maxoutput)

    def __str__(self):
        return f"House:{self.id}\nx: {self.x}\ny: {self.y}\nmaxoutput: {self.maxoutput}\n"   

    def get_id(self):
        return self.id
    
    def get_coord(self):
        return self.x, self.y
    
    def get_max(self):
        return self.maxoutput



    
    
class House:

    def __init__(self,id, x, y, maxoutput):
        self.id = id
        self.x = x
        self.y = y
        self.maxoutput = maxoutput

    def __str__(self):
        return f"House:{self.id}\nx: {self.x}\ny: {self.y}\nmaxoutput: {self.maxoutput}\n"   


    
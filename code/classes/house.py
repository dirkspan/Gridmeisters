class House:

    def __init__(self,id, x, y, maxoutput):
        self.id = id
        self.x = x
        self.y = y
        self.maxoutput = maxoutput

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x},y: {self.y},maxoutput: {self.maxoutput}"    


    
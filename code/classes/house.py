import battery

class House(object):

    def __init__(self,id, x, y, maxoutput):
        self.id = id
        self.x = x
        self.y = y
        self.maxoutput = maxoutput
        self.manhattan_distance = []
        self.connected_to = None

    def connect_to_battery(self, battery):
        self.connected_to = battery

    def __str__(self):
        return f"House:{self.id}\nx: {self.x}\ny: {self.y}\nmaxoutput: {self.maxoutput}\nbattery:{self.connected_to}"   




    
    
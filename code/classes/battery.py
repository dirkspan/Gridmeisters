class Battery:

    def __init__(self, id, x, y, capaciteit):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.capaciteit = float(capaciteit)

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapaciteit: {self.capaciteit}\n"       

        
    
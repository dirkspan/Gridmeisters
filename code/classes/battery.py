class Battery:

    def __init__(self, id, x, y, capaciteit):
        self.id = id
        self.x = x
        self.y = y
        self.capaciteit = capaciteit

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapaciteit: {self.capaciteit}\n"       

        
    
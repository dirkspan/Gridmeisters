class Battery:

    def __init__(self, id, x, y, capacity):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.capacity = capacity

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapaciteit: {self.capacity}\n"       

    def get_id(self):
        return self.id

    def get_coord(self):
        return self.x, self.y

    def get_cap(self):
        return self.capacity

    # set mothodes
    def set_coord(self, x, y):
        self.x = x
        self.y = y

    # capacity funtions

class CBar:
    def __init__(self):
        self.data = [['a', 'b', 'c'], [1, 2, 3], [1.1, 1.2, 1.3]]
        self.a = []
        self.b = []
        self.c = []
        
        self.create()

    def create(self):
        for item in self.data:
            self.a.append(item[0])
            self.b.append(item[1])
            self.c.append(item[2])
        

cbar = CBar()
print(cbar.a)
print(cbar.b)
print(cbar.c)

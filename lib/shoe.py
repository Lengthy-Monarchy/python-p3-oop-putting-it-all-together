class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self.size = size
    
    def cobble(self):
        print("The shoe has been repaired.")
        self.condition = "New"

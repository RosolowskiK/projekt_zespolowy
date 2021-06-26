class Barrier:
    open = False;

    def __init__(self):
        pass

    def open(self):
        self.open = True;
        print("The barrier opens")

    def close(self):
        self.open = False;
        print("The barrier closes")

    def is_open(self):
        return self.open


class Barrier:
    openStatus = False;

    def __init__(self):
        pass

    def open(self):
        self.openStatus = True;
        print("The barrier opens")

    def close(self):
        self.openStatus = False;
        print("The barrier closes")

    def is_open(self):
        return self.openStatus


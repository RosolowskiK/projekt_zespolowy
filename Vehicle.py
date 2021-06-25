import random


class Vehicle:

    def __init__(self):
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
        self.car_color = colors[random.randrange(0, len(colors))]
        self.car_number = "WKZ " + str(random.randrange(1000, 10000))

    def __str__(self):
        return f'Color: {self.car_color}, Number: {self.car_number}'

import random


class Controller:
    cars = []

    def __init__(self):
        pass

    def get_cars_in_parking(self):
        return self.cars

    def get_random_cart_in_parking(self):
        return self.cars[random.randrange(0, len(self.cars))]

    def car_in(self, car):
        self.cars.append(car)

    def car_out(self, car):
        self.cars.remove(car)


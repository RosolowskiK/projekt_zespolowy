from Vehicle import Vehicle
import random
import json


class Camera:
    # auto = Vehicle()

    def __init__(self, controller):
        self.controller = controller

    def car_in(self):
        car = Vehicle()
        self.controller.car_in(car)

    def car_out(self):
        car = self.controller.get_random_cart_in_parking()
        self.controller.car_out(car)


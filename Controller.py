from Barrier import Barrier
from Vehicle import Vehicle
from Terminal import Terminal
import random
import time


class Controller:
    cars = []

    def __init__(self):
        self.barrier = Barrier()
        pass

    def get_cars_in_parking(self):
        return self.cars

    def get_random_cart_in_parking(self):
        return self.cars[random.randrange(0, len(self.cars))]

    def car_in(self, car):
        self.cars.append(car)
        self.barrier.open()
        time.sleep(3)
        self.barrier.close()

    def car_out(self, car: Vehicle):
        car.set_parking_cost()
        terminal = Terminal(car)
        while not terminal.payment_successful:
            terminal.parking_fee()
        self.barrier.open()
        self.cars.remove(car)
        time.sleep(3)
        self.barrier.close()


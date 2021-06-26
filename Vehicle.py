from Printer import Printer
from random import randint
import random
from datetime import datetime, timedelta


class Vehicle:

    def __init__(self):
        self.printer = Printer()
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
        self.car_color = colors[random.randrange(0, len(colors))]
        self.car_number = "WKZ " + str(random.randrange(1000, 10000))
        self.time_start = datetime.today()
        self.parking_cost = 0
        self.parking_is_paid = False
        print(f'parking start time: {self.time_start}')

    def __str__(self):
        return f'Color: {self.car_color}, Number: {self.car_number}, Parking start: {self.time_start}'

    def get_time_start(self):
        return self.time_start

    def get_parking_cost(self):
        return self.parking_cost

    def get_parking_time(self):
        time_out = datetime.today()
        add_to_parking_time = randint(20, 1000)
        time_out += timedelta(minutes=add_to_parking_time)
        parking_time = (time_out - self.time_start)
        parking_time_second = parking_time.total_seconds()

        return parking_time_second / 60

    def set_parking_cost(self):
        parking_cost = self.printer.get_parking_cost(self)
        self.parking_cost = parking_cost

    def paid_for_parking(self, terminal):
        terminal.pay(self.parking_cost)

import sys


class Printer:

    def __init__(self):
        self.paring_cost = {
            (0, 30): 1,  # 0 to half hour
            (31, 60): 2,  # half hour to 1 hour
            (61, 120): 3,  # 1 hour to 2 hours
            (121, 180): 4,  # 1 hour to 2 hours
            (181, 300): 6,  # 3 hours to 5 hours
            (301, 1440): 10,  # 5 hours to 1 day
            (1441, 7200): 30,  # 1 day to 5 days
            (7201, sys.maxsize): 150  # 5 days to inf
        }

    def get_parking_cost(self, vehicle):
        parking_time = vehicle.get_parking_time()
        for times, cost in self.paring_cost.items():
            if times[0] <= parking_time <= times[1]:
                return cost

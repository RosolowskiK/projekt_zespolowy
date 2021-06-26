from Vehicle import Vehicle


class Terminal:

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.to_pay = vehicle.get_parking_cost()
        self.payment_successful = False

    def pay(self, value):
        print(f'to pay: {self.to_pay}, customer pays: {value}')
        self.to_pay -= value
        if self.to_pay == 0:
            self.payment_successful = True

    def set_to_pay(self, value):
        self.to_pay = value

    def parking_fee(self):
        self.vehicle.paid_for_parking(self)

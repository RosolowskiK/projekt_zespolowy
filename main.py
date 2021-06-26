from Controller import Controller
from Camera import Camera

if __name__ == '__main__':
    parking_open = True
    controller = Controller()
    camera = Camera(controller)

    while parking_open:
        command = input()

        if command == 'in':
            camera.car_in()
        elif command == 'out':
            camera.car_out()
        elif command == 'list':
            for car in controller.get_cars_in_parking():
                print(car)
        elif command == 'close':
            parking_open = False

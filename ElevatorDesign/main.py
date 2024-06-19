from request import Request
from controller import Controller

if __name__ == "__main__":
    print("Enter number of elevators")
    total_elevators = int(input())
    print("Enter number of floors")
    total_floors = int(input())
    controller = Controller(total_elevators, total_floors)

    while True:
        print("Request Floor")
        requested_floor = int(input())

        if requested_floor >  controller.total_floors or requested_floor <  0:
            print("Invalid request")
        
        else:
            controller.handle_request(Request(requested_floor))
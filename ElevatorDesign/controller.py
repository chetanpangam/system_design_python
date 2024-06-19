
from elevator import Elevator
import time
class Controller:
    def __init__(self, total_elevators, total_floors):
        self.total_floors = total_floors
        self.total_elevators = total_elevators
        self.elevators = [Elevator(i, self.total_floors) for i in range(self.total_elevators)]
        self.request_served = False
    
    def handle_request(self, request):
        for elevator in self.elevators:
            if elevator.current_floor == request.requested_floor:
                elevator.openDoor()
                time.sleep(2)
                elevator.closeDoor()
            
            elif elevator.current_floor < request.requested_floor:
                while elevator.current_floor != request.requested_floor:
                    elevator.moveUp()
                elevator.openDoor()
                self.request_served = True
                time.sleep(1)
                elevator.closeDoor()
            elif elevator.current_floor > request.requested_floor:
                while elevator.current_floor != request.requested_floor:
                    elevator.moveDown()
                elevator.openDoor()
                self.request_served = True
                time.sleep(1)
                elevator.closeDoor()

            if self.request_served:
                break


class Elevator:
    def __init__(self, id, total_floors):
        self.id = id
        self.total_floors = total_floors
        self.current_floor = 0
        
    def moveUp(self):
        if self.current_floor < self.total_floors:
            self.current_floor += 1

    def moveDown(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def openDoor(self):
        print(f"Opening Elevator {self.id}")

    def closeDoor(self):
        print(f"Closing Elevator {self.id}")
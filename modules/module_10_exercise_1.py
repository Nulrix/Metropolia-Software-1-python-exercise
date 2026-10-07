# Module 10 - Exercise 1: Elevator
# Program with an Elevator class that moves one floor at a time to the wanted floor


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print(f"Floor {floor} does not exist.")
        else:
            while self.current_floor < floor:
                self.floor_up()
            while self.current_floor > floor:
                self.floor_down()

    def floor_up(self):
        self.current_floor += 1
        print(f"The elevator is on floor {self.current_floor}.")

    def floor_down(self):
        self.current_floor -= 1
        print(f"The elevator is on floor {self.current_floor}.")


h = Elevator(1, 10)

print("Going up to floor 5:")
h.go_to_floor(5)

print("\nGoing back to the bottom floor:")
h.go_to_floor(h.bottom_floor)

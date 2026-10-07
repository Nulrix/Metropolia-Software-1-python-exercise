# Module 10 - Exercise 3: Fire Alarm
# Program where a fire alarm moves all elevators of the building to the bottom floor


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


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator {elevator_number} does not exist.")
        else:
            print(f"\nElevator {elevator_number} goes to floor {destination_floor}:")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators go to the bottom floor.")
        for i in range(len(self.elevators)):
            print(f"\nElevator {i + 1}:")
            self.elevators[i].go_to_floor(self.bottom_floor)


building = Building(1, 8, 3)

building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.run_elevator(3, 3)

building.fire_alarm()

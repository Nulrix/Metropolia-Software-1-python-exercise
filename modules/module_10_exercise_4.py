# Module 10 - Exercise 4: Race Class
# Program where a Race object runs the Grand Demolition Derby with ten cars

import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"{self.name} ({self.distance} km)")
        print(f"{'Car':<10}{'Max speed':>12}{'Speed':>10}{'Distance':>12}")
        print("-" * 44)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.max_speed:>7} km/h{car.current_speed:>5} km/h{car.travelled_distance:>9} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
finished = False
while not finished:
    race.hour_passes()
    hours += 1
    finished = race.race_finished()
    # status every ten hours (the final status is printed after the loop)
    if hours % 10 == 0 and not finished:
        print(f"\nStatus after {hours} hours:")
        race.print_status()

print(f"\nThe race is over after {hours} hours! Final status:")
race.print_status()

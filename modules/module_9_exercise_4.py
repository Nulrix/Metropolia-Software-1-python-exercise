# Module 9 - Exercise 4: Car Race
# Program where 10 cars race until one of them has driven at least 10 000 km

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


cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

hours = 0
race_over = False
while not race_over:
    hours += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_over = True

print(f"The race ended after {hours} hours.\n")
print(f"{'Car':<10}{'Max speed':>12}{'Speed':>10}{'Distance':>12}")
print("-" * 44)
for car in cars:
    print(f"{car.registration_number:<10}{car.max_speed:>7} km/h{car.current_speed:>5} km/h{car.travelled_distance:>9} km")

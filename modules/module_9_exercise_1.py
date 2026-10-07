# Module 9 - Exercise 1: Car Class
# Program that creates a car and prints out all of its properties


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


car = Car("ABC-123", 142)

print(f"Registration number: {car.registration_number}")
print(f"Maximum speed: {car.max_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")

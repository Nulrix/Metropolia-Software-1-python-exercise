# Module 9 - Exercise 3: Drive Method
# Program that adds the distance driven in a given number of hours to the travelled distance


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
        # distance = speed * time
        self.travelled_distance += self.current_speed * hours


car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed: {car.current_speed} km/h")

car.accelerate(-200)
print(f"Final speed: {car.current_speed} km/h")

car.accelerate(60)
car.drive(1.5)
print(f"After driving 1.5 hours at {car.current_speed} km/h the travelled distance is {car.travelled_distance} km.")

# Module 9 - Exercise 2: Accelerate Method
# Program that changes the speed of a car while keeping it between 0 and the maximum speed


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        # the speed can't go over the maximum or under zero
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0


car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed: {car.current_speed} km/h")

# emergency brake
car.accelerate(-200)
print(f"Final speed: {car.current_speed} km/h")

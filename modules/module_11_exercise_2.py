# Module 11 - Exercise 2: Electric And Gasoline Cars
# Program where ElectricCar and GasolineCar inherit the Car class


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


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        # the base class sets the registration number and maximum speed
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(120)
gasoline_car.accelerate(100)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car {electric_car.registration_number} ({electric_car.battery_capacity} kWh): {electric_car.travelled_distance} km")
print(f"Gasoline car {gasoline_car.registration_number} ({gasoline_car.tank_volume} l): {gasoline_car.travelled_distance} km")

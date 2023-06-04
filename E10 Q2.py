class Vehicle():

  color = "white"

  def __init__(self, name, max_speed, mileage):

    self.name = name

    self.max_speed = max_speed

    self.mileage = mileage



  def seating_capacity(self, capacity):

    return f"Seating capacity of {self.name} is {capacity} people"

class Bus(Vehicle):

  def seating_capacity(self, capacity=50):

    return super().seating_capacity(capacity=50)

bus = Bus("Volvo ", 200, 18)

print("Vehicle Name:", bus.name, "Speed:", bus.max_speed, "Mileage:",  bus.mileage)

print(bus.seating_capacity())
print("Colour of the bus is:",bus.color)

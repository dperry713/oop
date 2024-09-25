class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# Demonstration script
# Creating instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

# Displaying initial owners
print(f"Vehicle 1 initial owner: {vehicle1.owner}")
print(f"Vehicle 2 initial owner: {vehicle2.owner}")

# Updating owners
vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

# Displaying updated owners
print(f"Vehicle 1 new owner: {vehicle1.owner}")
print(f"Vehicle 2 new owner: {vehicle2.owner}")

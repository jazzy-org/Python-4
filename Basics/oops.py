# Defining our Car class
class Car:

    # Class Attribute
    car_type = 'Sedan'

    # Initializer attributes
    def __init__(self, fuel_type, model):
        self.fuel_type = fuel_type
        self.model = model

    # instance method
    def about(self):
        return f"My car is a {} {} and it runs on {}".(car_type, self.model, self.fuel_type)


# Instantiate the Car class
vishal_car = Car('petrol', 'R8')

# Now lets call our methods
print(vishal_car.about())
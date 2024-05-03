

class RentalCar():

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_available = True

    def get_info(self):
        return f'{self.color} {self.year} {self.make} {self.model}.'
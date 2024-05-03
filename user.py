
class User():

    def __init__(self, name, address, phone, rental_car=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.rental_car = rental_car

    def get_info(self):
        print(f'User: {self.name}')
        print(f'Address: {self.address}')
        print(f'Phone: {self.phone}')

    def rent(self, car):

        if self.rental_car != None:
            print('You cant rent two cars!')
            return
        else:
            self.rental_car = car
            car.is_available = False
            print(f'{self.name} has rented the {car.get_info()}')
    
    def return_car(self):
        self.rental_car.is_available = True
        print(f'{self.name} returned the {self.rental_car.get_info()}')
        self.rental_car = None

from user import User
from car import RentalCar

dylan = User('Dylan Katina', '123 Taco St.', '1234567890')
travis = User('Travis Peck', '456 Key Lime Cr.', '0987654321')

ferrari = RentalCar('Ferrari', 'Spider', '2023', 'Cherry Red')
mazda = RentalCar('Mazda', 'CX-30', '2022', 'Grey')
joe = RentalCar('Tesla', 'Model-X', '2024', 'Chrome')
BMW = RentalCar('BMW', 'M3', '2023', 'Black')
Mercedes = RentalCar('Mercedes', 'GLE65', '2023', 'Black')


def main():
    #you would have a database to pull
    cars = [ferrari, mazda, joe, BMW, Mercedes]
    users = [dylan, travis]
    current_user = None

    while True: 
        print(cars)
        action = input('''
    1.) User Actions                 
    2.) Rental Actions
    3.) Add Car
    4.) Quit
    > ''')
        
        if action == '1':
            current_user = user_functions(users)
        elif action == '2':
            current_user = rental_functions(cars, current_user)
        elif action == '3':
            make = input('Make: ')
            model = input('Model: ')
            year = input('Year: ')
            color = input('Color: ')
            new_car = RentalCar(make, model, year, color)
            print('Car Added to fleet!')
            cars.append(new_car)
        elif action == '4':
            break
        else:
            print('Invalid input, please use 1 ,2 ,3 ,4')


def user_functions(users):

    while True:
        action = input('''
    1.) Search User
    2.) Add User
    3.) Main Menu
    > ''')    

        if action == '1':
            user = search_users(users)
            return user
        elif action == '2':
            new_user = add_user()
            users.append(new_user)
            return new_user

        elif action == '3':
            break
        else:
            print('Invalid input, please use 1 ,2 ,3')
        #throw a flag to terminate main from child

def add_user():
    name = input('Name: ').title()
    address = input('Address: ').title()
    phone = input('Phone: ')
    new_user = User(name, address, phone)
    print('User Created')
    new_user.get_info()
    return new_user

def search_users(users):

    while True:
        name = input('Search Name: ').title()
        for user in users:
            if user.name == name:
                print('User Found!')
                user.get_info()
                return user
        
        action = input('No Response... try another name? y or n: ')
        if action == 'n':
            add_user()
        elif action == 'y':
            continue


def rental_functions(cars, current_user):

    while True:
        action = input('''
    1.) Rent Vehicle
    2.) Return Vehicle
    3.) Main Menu
''')
    
        if action == '1':
            for idx, car in enumerate(cars):
                if car.is_available:
                    print(f'{idx+1}.) {car.get_info()}') # 1.) car
            car_num = int(input('Car Number: ')) 
            car = cars[car_num - 1] 
            current_user.rent(car)
            return None
        elif action == '2':
            if current_user.rental_car:
                current_user.return_car()
                return None
            else:
                print('You dont have a car to return')
                return current_user

        elif action == '3':
            return current_user
        else:
            print('Invalid input, please use 1 ,2 ,3')  
            
            
        

    




main()

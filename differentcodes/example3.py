from datetime import datetime
class User:
    def __init__(self, first_name, last_name, driver_id, driver_category, birthday):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__driver_id = driver_id
        self.__driver_category = driver_category
        self.__birthday = birthday
    def get_fullname(self):
        return f"{self.__first_name} {self.__last_name}"
    def get_driver_id(self):
        return self.__driver_id
    def get_driver_category(self):
        if self.__driver_category:
            return self.__driver_category
        else:
            return ""
    def get_birthday(self):
        return self.__birthday
    def define_age(self):
        current_dt = datetime.today()
        birthday_dt = datetime.strptime(self.get_birthday(), "%Y-%m-%d")
        age = current_dt.year - birthday_dt.year
        if current_dt.month < birthday_dt.month \
                or (current_dt.month == birthday_dt.month and current_dt.day < birthday_dt.day):
            age -= 1
        return age
    def __str__(self):
        return f"----------------------------------\n" \
               f"first_name: {self.__first_name},\n" \
                f"first_name: {self.__first_name},\n" \
                f"last_name: {self.__last_name},\n" \
                f"driver_id: {self.__driver_id},\n" \
                f"driver_category: {self.__driver_category},\n" \
                f"birthday: {self.__birthday}\n" \
               f"--------------------------------- \n"
class Vehicle:
    def __init__(self, vehicle_id, brand, color):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.color = color
        self.is_rented = False
        self.renter = None
    def return_vehicle(self):
        if self.is_rented:
            print(f"Vehicle {self.vehicle_id} has been returned by {self.renter}")
            self.is_rented = False
            self.renter = None
        else:
            print(f"Vehicle {self.vehicle_id} is not nobody rented to return")
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, color, engine_type):
        super().__init__(vehicle_id, brand, color)
        self.engine_type = engine_type
    def rent(self, user):
        if not self.is_rented:
            if user.get_driver_id() and "B" in user.get_driver_category().upper():
                self.is_rented = True
                self.renter = user.get_fullname()
                print(f"Car {self.vehicle_id} has been taken by {self.renter} user")
            else:
                print(f"User {user.get_fullname()} does not have appropriate permission to drive a Car")
        else:
            print(f"Car {self.vehicle_id} has already rented")
    def __str__(self):
        return f"Vehicle_id: {self.vehicle_id}, Brand: {self.brand}, " \
               f"Color: {self.color}, Engine type: {self.engine_type}, Is rented: {self.is_rented}, " \
               f"Rented by: {self.renter}"
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, color, engine_capacity):
        super().__init__(vehicle_id, brand, color)
        self.engine_capacity = engine_capacity
    def rent(self, user):
        if not self.is_rented:
            if user.get_driver_id() and "A" in user.get_driver_category().upper():
                self.is_rented = True
                self.renter = user.get_fullname()
                print(f"Motorcycle {self.vehicle_id} has been taken by {self.renter} user")
            else:
                print(f"User {user.get_fullname()} does not have appropriate permission to drive a Motorcycle")
        else:
            print(f"Motorcycle {self.vehicle_id} has already rented")
    def __str__(self):
        return f"Vehicle_id: {self.vehicle_id}, Brand: {self.brand}, " \
               f"Color: {self.color}, Engine capacity: {self.engine_capacity}, Is rented: {self.is_rented}, " \
               f"Rented by: {self.renter}"
class Bicycle(Vehicle):
    def __init__(self, vehicle_id, brand, color, gears):
        super().__init__(vehicle_id, brand, color)
        self.gears = gears
    def rent(self, user):
        if not self.is_rented:
            if user.define_age() >= 14:
                self.is_rented = True
                self.renter = user.get_fullname()
                print(f"Bicycle {self.vehicle_id} has been taken by {self.renter} user")
            else:
                print(f"User {user.get_fullname()} does not have appropriate permission to drive a Bicycle")
        else:
            print(f"Bicycle {self.vehicle_id} has already rented")
    def __str__(self):
        return f"Vehicle_id: {self.vehicle_id}, Brand: {self.brand}, " \
               f"Color: {self.color}, Gears: {self.gears}, Is rented: {self.is_rented}, " \
               f"Rented by: {self.renter}"
class ElectricScooter(Vehicle):
    def rent(self, user):
        if not self.is_rented:
            if user.define_age() >= 14:
                self.is_rented = True
                self.renter = user.get_fullname()
                print(f"ElectricScooter {self.vehicle_id} has been taken by {self.renter} user")
            else:
                print(f"User {user.get_fullname()} does not have appropriate permission to drive an ElectricScooter")
        else:
            print(f"ElectricScooter {self.vehicle_id} has already rented")
    def __str__(self):
        return f"Vehicle_id: {self.vehicle_id}, Brand: {self.brand}, " \
               f"Color: {self.color}, Is rented: {self.is_rented}, " \
               f"Rented by: {self.renter}"
user_1 = User("Ivan", "Borodii", "ABC111", "A/B", "2020-04-19")
car_1 = Car("AAA", "Volvo", "Yellow", "Electro")
car_2 = Car("BBB", "Toyota", "Green", "Disel")
motorcycle_1 = Motorcycle("CCC", "Kawasaki", "Orange", "100")
motorcycle_2 = Motorcycle("DDD", "Honda", "Blue", "250")
bicycle_1 = Bicycle("SSS", "Volvo", "Yellow", "3")
bicycle_2 = Bicycle("UUU", "Ford", "Red", "22")
scooter_1 = ElectricScooter("iii", "Bolt", "Green")
scooter_2 = ElectricScooter("kkk", "Jet", "Blue")
car_1.rent(user_1)
car_2.rent(user_1)
motorcycle_1.rent(user_1)
motorcycle_2.rent(user_1)
bicycle_1.rent(user_1)
bicycle_2.rent(user_1)
scooter_1.rent(user_1)
scooter_2.rent(user_1)
car_1.return_vehicle()
car_2.return_vehicle()
motorcycle_1.return_vehicle()
motorcycle_2.return_vehicle()
bicycle_1.return_vehicle()
bicycle_2.return_vehicle()
scooter_1.return_vehicle()
scooter_2.return_vehicle()
scooter_2.return_vehicle()
print(scooter_1)
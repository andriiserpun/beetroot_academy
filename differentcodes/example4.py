class Electricity:
    def __init__(self, number, unit):
        self.number = number
        self.unit = unit
    def info(self):
        print("Будь зі мною обережний, а то я вдарю струмом.. .")
    def make_sound(self):
        print("дзззззззззззззззззз")
    def print_usage(self):
        print(f"за цей місяць ти мене насвітив на {self.number} {self.unit}")
class Water:
    def __init__(self, number, unit):
        self.number = number
        self.unit = unit
    def info(self):
        print("з крану мене пити не можна")
    def make_sound(self):
        print("пшшшшшшшшшшшшшшшшшш")
    def print_usage(self):
        print(f"за цей місяць ти помився на {self.number} {self.unit}")
electricity = Electricity(150, "Watt")
water = Water(3, "Cubic meter")
comunalka = [electricity, water]
for item in comunalka:
    item.info()
    item.make_sound()
    item.print_usage()
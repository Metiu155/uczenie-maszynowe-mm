class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f'{self.area}, {self.rooms}, {self.price}, {self.address}'
    

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int,):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        
    def __str__(self):
         return super().__str__() + f' {self.plot}'

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area,rooms,price,address)
        self.floor = floor

    def __str__(self):
         return super().__str__() + f'{ self.floor}'

House1 = House("Mikolow",10,"65$","Katowicka 10",2)
Flat1 = Flat("Kokolow",4,"23$","Buby 10",3)

print(House1)
print(Flat1)

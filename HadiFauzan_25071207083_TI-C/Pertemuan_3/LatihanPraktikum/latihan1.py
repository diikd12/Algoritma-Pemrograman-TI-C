class Vehicle:
    def __init__(self, type, brand, releaseYear):
        self.type = type
        self.brand = brand
        self.__releaseYear = releaseYear

    def sound(self):
        return ('suara.')
    
    def get_Year(self):
        return self.__releaseYear
    
    def set_year(self, new):
        self.__releaseYear = new
        print('tahun produksi berhasil di ubah menjadi')
    

class Car(Vehicle):
    def __init__(self, type, brand, releaseYear):
        super().__init__(type, brand, releaseYear)
    
    def printCar(self):
        print (self.type, self.brand, self._Vehicle__releaseYear)

class Bike(Vehicle):
    def __init__(self, type, brand, releaseYear):
        super().__init__(type, brand, releaseYear)

    def printBike(self):
        print (self.type, self.brand, self._Vehicle__releaseYear)

car1 = Car('sedan', 'BMW M4 Competition', '2014')
bike1 = Bike('sport', 'Duvati Panigale V4S', '2018')

for x in (car1, bike1):
    print (x.sound())

car1.printCar()
bike1.printBike()
car1.set_year(2025)
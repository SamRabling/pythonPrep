class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = ''
    
    def displayAll(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Milage: " + str(self.mileage)
        if self.price < 10000:
            print "Tax: " + '12%'
        if self.price > 10000:
            print "Tax: " + '15%'


car1 = Car(5000, '200mph', 'Full', '40mpg')
car2 = Car(6000, '160mph', 'Not Full', '70mpg')
car3 = Car(18000, '180mph', 'Full', '42mpg')
car4 = Car(5000, '160mph', 'Full', '28mpg')
car5 = Car(2000, '100mph', 'Not Full', '54mpg')
car6 = Car(12000, '300mph', 'Not Full', '70mpg')

print Car.displayAll(car1)
print Car.displayAll(car2)
print Car.displayAll(car3)
print Car.displayAll(car4)
print Car.displayAll(car5)
print Car.displayAll(car6)

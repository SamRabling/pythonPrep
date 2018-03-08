class Bike(object):                        #This is a new class
    def __init__(self, price, max_speed):    #
        self.price = price                    #   
        self.max_speed = max_speed            #This are the attributes
        self.miles = 0                    #

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        self.miles += 10
        print 'Riding'
        return self

    def reverse(self):
        self.miles -= 5
        print 'Reversing'
        if self.miles < 0:
            self.miles = 0
        return self

trek = Bike(400, '50mph')                   #
cannondale = Bike(550, '55mph')            #This are the new instances
schwinn = Bike(800, '65mph')

print trek.ride().ride().ride().reverse().displayInfo()
print cannondale.ride().ride().reverse().reverse().displayInfo()
print schwinn.reverse().reverse().reverse().displayInfo()

class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = ''
        self.tax = ''
    
    def selling(self):
        self.status = 'Sold'
        return self.status

    def addTax(self):
        self.tax = self.price * .08
        return self.tax

    def returnedItem(self, reason, box):
        if reason == 'defective':
            self.price = 0
            self.status = 'defective'
        elif reason == 'returning':
            if box == 'closed':
                self.status = 'For Sale'
        if reason == 'returning':
            if box == 'opened':
                self.status = 'Used'
                self.price = price - (price * .20)
    

    def displayInfo(self):
        self.addTax()
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brande: " + str(self.brand)
        print "Status:" + str(self.status)
        print "Tax: " + str(self.tax)

prod1 = Product(40, 'name', '1lb', 'Fancy Brand', 'defective' )
# prod2 = 
# prod3 = 
# prod4 = 

print Product.displayInfo(prod1)
    
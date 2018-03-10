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
        return self

        

    def addTax(self):
        self.tax = self.price * .08
        return self.tax

    def returnedItem(self, reason):
        if "defective" in reason:
            self.price = 0
            self.status = "defective"
        elif "returning_close" in reason:
            self.status = "For Sale"
        elif "returning_open" in reason:
            self.status = "Used"
            self.price = price - (price * .20)
        else:
            "For Sale" in self.status 
        return self

        self.returnedItem('new')
        self.selling()   

    def displayInfo(self):
        print("Name: {}, Price: ${}, Weight: {}, Brand: {}, Status: {}, Tax: ${}".format(
        self.item_name, self.price, self.weight, self.brand, self.status, self.addTax()))
    
        
        # print "Price: " + str(self.price)
        # print "Item Name: " + str(self.item_name)
        # print "Weight: " + str(self.weight)
        # print "Brand: " + str(self.brand)
        # print "Status:" + str(self.status)
        # print "Tax: " + str(self.tax)

prod1 = Product(40, 'name', '1lb', 'Fancy Brand', 'new')

# prod2 = 
# prod3 = 
# prod4 = 

print Product.displayInfo(prod1)
    
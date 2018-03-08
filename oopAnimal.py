class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.health
        return self

bear = Animal('Sawyer', 29)
print bear.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def set_health(self):
        self.health = 150
        return self

    def pet(self):
        self.health += 5
        return self

shiba = Dog('Alot',150)
print shiba.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def set_health(self):
        self.health = 170
        return self

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "I am a Dragon" + str(self.health)
        return self

Norwegian_Ridgeback = Dragon('Norbert', 150)
print Norwegian_Ridgeback.fly().fly().displayHealth()
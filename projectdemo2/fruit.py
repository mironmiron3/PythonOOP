from projectdemo2.food import Food

class Fruit(Food):
    def __init__(self,name, expiration_date):
        Food.__init__(expiration_date)
        self.name = name
    pass

f = Fruit("banana", "2020")
print(f.name,f.expiration_date)
f = Fruit("kiwi","2020")
print(f.expiration_date)
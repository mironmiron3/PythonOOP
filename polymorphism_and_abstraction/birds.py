from wild_farm.animal import Animal
from wild_farm.food import Meat
from wild_farm.food import Seed
#from wild_farm.mammals import Mammal
#from wild_farm.mammals import Mouse


class Bird(Animal):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def make_sound(self):
        pass


    def feed(self, food):
        pass

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Owl(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.25


class Hen(Bird):
    #def __init__(self, name, weight, food_eaten, wing_size):
        #super().__init__(name, weight, food_eaten, wing_size)

    def make_sound(self):
        return "Cluck"

    #def feed(self, food):
        #pass

hen = Hen("kiro", 50, 10)
print(hen.weight)
hen.feed(Seed(5))
print(hen.weight)

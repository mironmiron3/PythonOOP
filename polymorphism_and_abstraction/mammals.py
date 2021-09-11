from wild_farm.animal import Animal
from wild_farm.birds import Owl
from wild_farm.food import Meat, Vegetable, Fruit


class Mammal(Animal):
    def __init__(self, name, weight,living_region, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def make_sound(self):
        pass

    def feed(self, food):
        pass

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Fruit) or not isinstance(food, Vegetable):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.10



class Dog(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Woof"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.4


class Cat(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Meat) or not isinstance(food, Vegetable):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.3



class Tiger(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 1

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

from abc import ABC, abstractmethod
food_mapper = {"Hen": (["Meat","Vegetable", "Fruit", "Seed"],0.35),"Mouse":(["Vegetable", "Fruit"], 0.10), "Cat":(["Vegatable","Meat"],0.30), "Tiger":(["Meat"],1),"Dog":(["Meat"], 0.4),"Owl":(["Meat"], 0.25)}


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass


    #@abstractmethod
    def feed(self, food):
        type_of_animal = type(self).__name__
        if type(food).__name__ in food_mapper[type_of_animal][0]:
            self.weight += food_mapper[type_of_animal][1]
        else:
            return f"{type(self).__name__} does not eat {food}!"

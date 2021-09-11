class Survivor:
    def __init__(self,name: str, age: int):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100
        #self.needs_sustenance = False
        #self.needs_healing = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value < 0 or value > 100:
            raise ValueError("Health not valid!")
        self.__health = value

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0 or value > 100:
            raise ValueError("Needs not valid!")
        self.__needs = value

    @property
    def needs_sustenance(self):
        return True if self.needs < 100 else False

    @property
    def needs_healing(self):
        return True if self.health < 100 else False




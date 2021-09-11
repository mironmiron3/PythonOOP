from animals.animal import Animal


class Cat(Animal):
    pass
    def make_sound(self):
        return "Meow meow!"

class Kitten(Cat):
    def __init__(self, name, age):
        super(Kitten, self).__init__(name, age, "Female")

    def make_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss"


kitty = Tomcat("Kiroo", 10)
print(kitty.make_sound())

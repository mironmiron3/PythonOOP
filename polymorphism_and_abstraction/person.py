class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)




##person1 = Person("kiro", "pedalski")
#person2 = Person("miro", "ivanov")
#print(person2)